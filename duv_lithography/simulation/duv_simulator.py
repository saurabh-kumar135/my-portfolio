#!/usr/bin/env python3
"""
duv_simulator.py — 193nm DUV Lithography Optical Simulation
============================================================
Pipeline:
  GDS file → extract polygons → rasterize mask →
  Fourier optics (aerial image) → resist threshold → printed pattern

Physics:
  - Coherent imaging: H(fx,fy) = 1 if sqrt(fx²+fy²) < NA/λ, else 0
  - Partially coherent: convolve aerial image with source shape
  - Aerial image: I(x,y) = |IFFT(H · FFT(mask))|²
  - Resist: exposed = I(x,y) > threshold

Target: SKY130 130nm node | NA=0.85 | λ=193nm | σ=0.7
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys
import os

try:
    import gdstk
    HAS_GDSTK = True
except ImportError:
    HAS_GDSTK = False

# ============================================================
# MACHINE PARAMETERS
# ============================================================
WAVELENGTH_NM = 193.0          # nm — ArF excimer laser
NA            = 0.85           # Numerical aperture
SIGMA         = 0.7            # Partial coherence factor
REDUCTION     = 4.0            # 4:1 reduction from mask to wafer
RESIST_THRESH = 0.35           # Normalized intensity threshold (0–1)
DOSE_MJ_CM2   = 25.0           # Exposure dose [mJ/cm²]

# Derived
LAMBDA = WAVELENGTH_NM * 1e-3  # µm
RESOLUTION = 0.5 * LAMBDA / NA  # Rayleigh criterion [µm]
DOF_UM = LAMBDA / (2 * NA**2)   # Depth of focus [µm]

print("=" * 60)
print("  DUV Lithography Simulator — 193nm ArF")
print("=" * 60)
print(f"  Wavelength  : {WAVELENGTH_NM} nm")
print(f"  NA          : {NA}")
print(f"  Sigma (σ)   : {SIGMA}")
print(f"  Resolution  : {RESOLUTION*1000:.1f} nm (Rayleigh 0.5λ/NA)")
print(f"  DoF         : ±{DOF_UM*1000:.0f} nm")
print(f"  Reduction   : {REDUCTION}:1")
print(f"  Resist thresh: {RESIST_THRESH}")
print("=" * 60)


# ============================================================
# STEP 1: GDS READER / POLYGON EXTRACTOR
# ============================================================
def _scanline_fill(poly_pts, Nx, Ny, xmin, xmax, ymin, ymax):
    """Fast scanline polygon fill — O(N·edges) instead of O(N·pixels)."""
    mask = np.zeros((Ny, Nx), dtype=np.uint8)
    px = (poly_pts[:, 0] - xmin) / (xmax - xmin) * (Nx - 1)
    py = (poly_pts[:, 1] - ymin) / (ymax - ymin) * (Ny - 1)
    n  = len(px)
    for row in range(Ny):
        xs_intersect = []
        for i in range(n):
            j = (i + 1) % n
            yi, yj = py[i], py[j]
            if (yi <= row < yj) or (yj <= row < yi):
                t   = (row - yi) / (yj - yi)
                xi  = px[i] + t * (px[j] - px[i])
                xs_intersect.append(xi)
        xs_intersect.sort()
        for k in range(0, len(xs_intersect) - 1, 2):
            x0 = int(np.floor(xs_intersect[k]))
            x1 = int(np.ceil(xs_intersect[k+1]))
            mask[row, max(0,x0):min(Nx,x1+1)] = 1
    return mask

def load_gds_layer(gds_file, layer_num, pixel_size_nm=10.0, canvas_um=None):
    """
    Read polygons from GDS layer and rasterize to binary numpy array.
    Fast path: uses gdstk flatten on TOP CELL ONLY, then scanline fill.
    Returns: (mask_array, extent_um)
    """
    if not HAS_GDSTK or not os.path.exists(gds_file):
        print(f"  [INFO] GDS not found — using synthetic CMOS inverter pattern")
        return _synthetic_inverter_mask(pixel_size_nm, canvas_um or 5.0)

    print(f"  Reading GDS: {gds_file}, layer {layer_num}")
    lib = gdstk.read_gds(gds_file)

    # Find top cell (the design, not library cells)
    top_cells = lib.top_level()
    if not top_cells:
        top_cells = lib.cells
    top_cell = top_cells[0]
    print(f"  Top cell: {top_cell.name}")

    # Flatten top cell — expands all sub-cell references in-place
    top_cell.flatten()

    # Collect polygons on the requested layer
    polys = [p.points for p in top_cell.polygons if p.layer == layer_num]
    if not polys:
        print(f"  [WARN] No polygons on layer {layer_num}. Using synthetic pattern.")
        return _synthetic_inverter_mask(pixel_size_nm, canvas_um or 5.0)

    print(f"  Found {len(polys)} polygons on layer {layer_num}")

    # Bounding box
    all_pts = np.vstack(polys)
    xmin, ymin = all_pts.min(axis=0)
    xmax, ymax = all_pts.max(axis=0)
    margin = 0.5
    xmin -= margin; ymin -= margin
    xmax += margin; ymax += margin

    pixel_um = pixel_size_nm / 1000.0
    Nx = min(int((xmax - xmin) / pixel_um), 512)  # cap at 512 for speed
    Ny = min(int((ymax - ymin) / pixel_um), 512)

    print(f"  Rasterizing {len(polys)} polygons → {Nx}×{Ny} grid...")
    mask = np.zeros((Ny, Nx), dtype=np.float32)
    for pts in polys:
        mask += _scanline_fill(pts, Nx, Ny, xmin, xmax, ymin, ymax)
    mask = np.clip(mask, 0, 1)
    print(f"  Mask ready. Non-zero pixels: {mask.sum():.0f} / {Nx*Ny}")
    return mask, (xmin, xmax, ymin, ymax)


def _synthetic_inverter_mask(pixel_size_nm=10.0, canvas_um=8.0):
    """
    Create a synthetic CMOS inverter mask pattern (poly gate layer).
    Features match SKY130 130nm design rules.
    """
    pixel_um = pixel_size_nm / 1000.0
    N = int(canvas_um / pixel_um)
    N = min(N, 512)
    mask = np.zeros((N, N), dtype=np.float32)
    um_per_px = canvas_um / N

    def fill_rect(mask, x0, y0, x1, y1, val=1.0):
        """Fill rectangle in µm coordinates."""
        ix0 = int(x0 / um_per_px)
        ix1 = int(x1 / um_per_px)
        iy0 = int(y0 / um_per_px)
        iy1 = int(y1 / um_per_px)
        mask[iy0:iy1, ix0:ix1] = val

    # PMOS source/drain active regions
    fill_rect(mask, 1.0, 5.5, 4.0, 7.2)
    # NMOS source/drain active regions
    fill_rect(mask, 1.0, 1.0, 4.0, 2.8)

    # Poly gate (crosses both transistors — 130nm width)
    fill_rect(mask, 1.8, 0.8, 1.93, 7.4)   # gate poly — 130 nm wide

    # Metal1 VDD rail (top)
    fill_rect(mask, 0.5, 7.0, 5.0, 7.4)
    # Metal1 GND rail (bottom)
    fill_rect(mask, 0.5, 0.5, 5.0, 0.9)
    # Metal1 output node
    fill_rect(mask, 4.5, 2.2, 5.0, 5.5)

    # Via holes (dark = transparent = open)
    for vy in [1.7, 6.5]:
        for vx in [4.3]:
            fill_rect(mask, vx, vy, vx+0.15, vy+0.15, 0.0)

    # Second poly gate (fan-out wire)
    fill_rect(mask, 3.0, 0.8, 3.13, 7.4)

    print(f"  Synthetic CMOS inverter mask: {N}×{N} px ({canvas_um} µm canvas)")
    return mask, (0, canvas_um, 0, canvas_um)


# ============================================================
# STEP 2: FOURIER OPTICS — AERIAL IMAGE
# ============================================================
def compute_aerial_image(mask, pixel_size_nm=10.0, sigma=SIGMA, na=NA, lam_nm=WAVELENGTH_NM):
    """
    Compute aerial image using partial-coherent Hopkins formalism (simplified).
    
    I_aerial(x,y) = Σ_{source pts s} |IFFT(CTF(s) · FFT(mask))|²
    
    Approximated here as:
    1. Coherent: I_c = |IFFT(CTF(fx,fy) · FFT(mask))|²
    2. Partially coherent: convolve I_c with source intensity distribution
    """
    Ny, Nx = mask.shape
    pixel_um = pixel_size_nm / 1000.0

    # Frequency axes (cycles/µm)
    dfx = 1.0 / (Nx * pixel_um)
    dfy = 1.0 / (Ny * pixel_um)
    fx  = np.fft.fftfreq(Nx, d=pixel_um)
    fy  = np.fft.fftfreq(Ny, d=pixel_um)
    FX, FY = np.meshgrid(fx, fy)
    F_r    = np.sqrt(FX**2 + FY**2)

    lam_um = lam_nm / 1000.0
    f_cutoff = na / lam_um   # cycles/µm

    # Coherent Transfer Function (pupil function)
    CTF = (F_r <= f_cutoff).astype(complex)

    # Apply CTF in frequency domain
    MASK_F    = np.fft.fft2(mask.astype(complex))
    AERIAL_F  = CTF * MASK_F
    aerial_c  = np.abs(np.fft.ifft2(AERIAL_F))**2

    # Partial coherence: source is disk of radius sigma·f_cutoff
    # Approximate: convolve coherent image with source image
    f_src = sigma * f_cutoff
    src_mask_f = (F_r <= f_src).astype(float)
    src_psf = np.abs(np.fft.ifft2(np.fft.fftshift(src_mask_f)))**2
    src_psf /= src_psf.sum()

    # Convolve aerial image with source PSF
    SRC_F    = np.fft.fft2(src_psf)
    AER_F    = np.fft.fft2(aerial_c)
    aerial   = np.real(np.fft.ifft2(AER_F * SRC_F))
    aerial   = np.fft.fftshift(aerial)

    # Normalize 0–1
    aerial -= aerial.min()
    if aerial.max() > 0:
        aerial /= aerial.max()

    return aerial


# ============================================================
# STEP 3: RESIST MODEL
# ============================================================
def apply_resist_model(aerial, threshold=RESIST_THRESH, blur_nm=20, pixel_size_nm=10):
    """
    Positive-tone chemically amplified resist model.
    1. Blur aerial image (acid diffusion during PEB)
    2. Apply threshold: exposed = aerial > threshold
    3. Returned: binary resist pattern (1=exposed=removed in positive resist)
    """
    from scipy.ndimage import gaussian_filter
    sigma_px = (blur_nm / pixel_size_nm)
    try:
        aerial_blurred = gaussian_filter(aerial, sigma=sigma_px)
    except Exception:
        aerial_blurred = aerial  # fallback if scipy unavailable

    resist = (aerial_blurred > threshold).astype(float)
    return resist, aerial_blurred

def apply_resist_model_noscipy(aerial, threshold=RESIST_THRESH, blur_nm=20, pixel_size_nm=10):
    """Resist model without scipy — use FFT-based Gaussian blur."""
    Ny, Nx  = aerial.shape
    sigma_px = blur_nm / pixel_size_nm
    # Gaussian kernel in frequency domain
    fy = np.fft.fftfreq(Ny)
    fx = np.fft.fftfreq(Nx)
    FX, FY  = np.meshgrid(fx, fy)
    G = np.exp(-2 * (np.pi * sigma_px)**2 * (FX**2 + FY**2))
    aerial_blurred = np.real(np.fft.ifft2(np.fft.fft2(aerial) * G))
    resist = (aerial_blurred > threshold).astype(float)
    return resist, aerial_blurred


# ============================================================
# STEP 4: VISUALIZE — 5-PANEL RESULT
# ============================================================
def visualize_results(mask, aerial, aerial_blurred, resist, extent, pixel_size_nm, out_path):
    fig, axes = plt.subplots(1, 5, figsize=(22, 6), facecolor='#0d1117')
    fig.suptitle('DUV 193nm Lithography Simulation — GDS → Aerial Image → Resist Pattern\n'
                 f'λ={WAVELENGTH_NM}nm | NA={NA} | σ={SIGMA} | Threshold={RESIST_THRESH} | '
                 f'Resolution={RESOLUTION*1000:.0f}nm',
                 color='white', fontsize=12, fontweight='bold')

    xmin, xmax, ymin, ymax = extent
    ext = [xmin, xmax, ymin, ymax]
    cmaps = ['gray', 'hot', 'plasma', 'RdBu_r', 'Greens']
    titles = [
        'MASK\n(GDS input)',
        'AERIAL IMAGE\n(coherent focus)',
        'AERIAL IMAGE\n(partial coherent)',
        'RESIST EXPOSURE\n(acid blur + dose)',
        'PRINTED PATTERN\n(final resist CD)'
    ]
    images = [mask, aerial, aerial_blurred,
              np.clip(aerial_blurred, 0, 1),
              resist]

    for ax, img, title, cmap in zip(axes, images, titles, cmaps):
        ax.set_facecolor('#161b22')
        im = ax.imshow(img, cmap=cmap, origin='lower',
                       extent=ext, aspect='equal', interpolation='bilinear')
        ax.set_title(title, color='white', fontsize=9, fontweight='bold')
        ax.set_xlabel('x (µm)', color='gray', fontsize=7)
        ax.set_ylabel('y (µm)', color='gray', fontsize=7)
        ax.tick_params(colors='gray', labelsize=6)
        for sp in ax.spines.values():
            sp.set_color('#30363d')
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04).ax.tick_params(colors='gray', labelsize=6)

    # Overlay CD measurement on last panel
    axes[4].set_title('PRINTED PATTERN\n(final resist CD — 130nm target)', 
                      color='white', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig(out_path, dpi=130, bbox_inches='tight', facecolor='#0d1117')
    print(f"  Output saved: {out_path}")
    plt.close()


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='DUV 193nm Lithography Simulator')
    parser.add_argument('--gds',     default='', help='Input GDS file path')
    parser.add_argument('--layer',   type=int, default=66, help='GDS layer number (default: 66=poly)')
    parser.add_argument('--pixel',   type=float, default=5.0, help='Pixel size in nm (default: 5)')
    parser.add_argument('--thresh',  type=float, default=RESIST_THRESH, help='Resist threshold 0-1')
    parser.add_argument('--out',     default='output/lithography_result.png', help='Output image path')
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.out) if os.path.dirname(args.out) else '.', exist_ok=True)

    print("\n[STEP 1] Loading GDS / generating mask...")
    mask, extent = load_gds_layer(args.gds, args.layer, args.pixel)

    print(f"\n[STEP 2] Computing aerial image (Fourier optics)...")
    print(f"  Mask size: {mask.shape}")
    aerial_coherent = compute_aerial_image(mask, args.pixel)
    print(f"  Aerial image computed. Min={aerial_coherent.min():.3f} Max={aerial_coherent.max():.3f}")

    print(f"\n[STEP 3] Applying resist model (threshold={args.thresh})...")
    try:
        resist, aerial_blurred = apply_resist_model(aerial_coherent, args.thresh, 
                                                     blur_nm=15, pixel_size_nm=args.pixel)
    except Exception:
        resist, aerial_blurred = apply_resist_model_noscipy(aerial_coherent, args.thresh,
                                                             blur_nm=15, pixel_size_nm=args.pixel)
    exposed_frac = resist.mean()
    print(f"  Exposed area: {exposed_frac*100:.1f}%")

    print(f"\n[STEP 4] Generating visualization...")
    visualize_results(mask, aerial_coherent, aerial_blurred, resist, extent, args.pixel, args.out)

    print("\n" + "=" * 60)
    print("  SIMULATION COMPLETE")
    print(f"  Theoretical resolution: {RESOLUTION*1000:.1f} nm")
    print(f"  Depth of focus:         ±{DOF_UM*1000:.0f} nm")
    print(f"  Output:                 {args.out}")
    print("=" * 60)
