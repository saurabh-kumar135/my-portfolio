# DUV Lithography Machine — 193nm ArF

A complete design and simulation of a **193nm Deep UV (DUV) ArF Excimer Lithography Machine** targeting the **SkyWater 130nm (SKY130) process node**.

## What's Inside

| File/Folder                              | Description                                 |
| ---------------------------------------- | ------------------------------------------- |
| `physical_design/machine_overview.png`   | Full system architecture — all 9 subsystems |
| `physical_design/optical_subsystem.png`  | Optical path + wafer stage + resist process |
| `physical_design/wafer_process.png`      | Silicon layer formation + step-and-scan map |
| `physical_design/cad_3d_isometric.png`   | 3D CAD isometric render of the machine      |
| `physical_design/cad_ortho_drawings.png` | Engineering drawings (front/side/top + BOM) |
| `simulation/duv_simulator.py`            | GDS → Aerial Image → Resist simulation      |
| `output/`                                | Simulation results                          |

---

## Machine Specifications

| Parameter          | Value                               |
| ------------------ | ----------------------------------- |
| Laser              | ArF Excimer, **193 nm**, 40W, 6 kHz |
| Numerical Aperture | **NA = 0.85**                       |
| Partial Coherence  | σ = 0.7                             |
| Resolution         | **113.5 nm** (0.5·λ/NA)             |
| Depth of Focus     | ±134 nm                             |
| Reduction Ratio    | 4:1                                 |
| Wafer Size         | 300 mm                              |
| Throughput         | ~150 wafers/hr                      |
| Overlay            | < 5 nm (3σ)                         |
| Machine Footprint  | 2.4m × 1.6m × 2.1m                  |
| Weight             | ~30,000 kg                          |

---

## Optical Simulation Pipeline

```
GDS File → Extract Polygons → Rasterize Mask
         → Fourier Optics (CTF) → Aerial Image
         → Partial Coherence (σ=0.7)
         → Resist Model (CAR + PEB blur)
         → Printed Pattern
```

### Physics

```
Coherent Transfer Function:
  CTF(fx, fy) = 1  if √(fx²+fy²) < NA/λ,  else 0

Aerial Image:
  I(x,y) = |IFFT(CTF · FFT(mask))|²

Resist:
  exposed(x,y) = 1  if gaussian_blur(I, σ_PEB) > threshold
```

---

## Run the Simulation

```bash
# Install dependencies
pip install gdstk matplotlib numpy

# Run on your own GDS file
python3 simulation/duv_simulator.py \
  --gds your_design.gds \
  --layer 66 \       # poly layer
  --pixel 5 \        # 5nm pixel size
  --thresh 0.35 \    # resist threshold
  --out output/result.png
```

---

## Machine Subsystems

1. **ArF Excimer Laser** — 193nm, 40W, 6kHz repetition rate
2. **Beam Delivery System** — expander + attenuator + homogenizer
3. **Illumination Optics** — Köhler illumination, fly-eye lens, σ=0.7
4. **Reticle Stage** — 6" chrome-on-quartz mask, ±0.5nm positioning
5. **Projection Lens** — NA=0.85, 30 fused silica + CaF₂ elements
6. **Wafer Stage** — 300mm Si wafer, XY piezo, 0.3nm resolution
7. **Alignment System** — TTL off-axis laser interferometry, <1nm overlay
8. **Environmental Control** — ±0.01°C, N₂ purge, vibration isolation
9. **Coat/Dev Track** — Spin coat CAR resist, TMAH develop

---

## Related Projects

- [`asic_inverter/`](../asic_inverter/) — Full ASIC flow: RTL → Synthesis → P&R → GDS → JEOL
- [`neural_electrode/`](../neural_electrode/) — 64-channel BCI electrode array design
- [`demo_ai_capability/`](../demo_ai_capability/) — RISC-V RV32I processor design

---

## Part of the Full ASIC Flow

```
RTL (Verilog) → Synthesis (Yosys+SKY130) → Place & Route (OpenROAD)
  → GDS (KLayout) → JEOL mask file → [THIS MACHINE] → Silicon wafer
```
