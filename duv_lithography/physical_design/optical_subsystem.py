import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(20, 11), facecolor='#0d1117')
fig.suptitle('DUV Optical System — Illumination Path & Projection Lens Cross-Section',
             color='white', fontsize=13, fontweight='bold')

# ============ LEFT: Full optical path (side view) ============
ax = axes[0]
ax.set_facecolor('#0d1117')
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 16)
ax.axis('off')
ax.set_title('Optical Path (Side View)', color='white', fontsize=10, fontweight='bold')

def comp_box(ax, x, y, w, h, color, label, detail=''):
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
        linewidth=1.5, edgecolor=color, facecolor='#161b22', alpha=0.9)
    ax.add_patch(r)
    ax.text(x+w/2, y+h/2+(0.1 if detail else 0), label,
            ha='center', va='center', color='white', fontsize=8, fontweight='bold')
    if detail:
        ax.text(x+w/2, y+h/2-0.2, detail, ha='center', va='center', 
                color='#8b949e', fontsize=6.5)

# ArF laser
comp_box(ax, 1.0, 14.5, 2.5, 0.8, '#ff6b35', 'ArF Laser (193 nm)', '40W | 6kHz | 1pm linewidth')
# Beam expander
comp_box(ax, 1.0, 13.2, 2.5, 0.8, '#ffd700', 'Beam Expander', '5× magnification')
# Attenuator
comp_box(ax, 1.0, 12.0, 2.5, 0.8, '#ffd700', 'Attenuator', 'Variable dose control')
# Homogenizer
comp_box(ax, 1.0, 10.8, 2.5, 0.8, '#ffd700', 'Fly-eye Lens', 'Köhler homogenizer')
# Condenser
comp_box(ax, 1.0, 9.6, 2.5, 0.8, '#39d353', 'Condenser Lens', 'Sets NA & sigma')
# Aperture stop
comp_box(ax, 1.0, 8.7, 2.5, 0.5, '#39d353', 'Illumination Aperture (σ=0.7)', '')
# Reticle
comp_box(ax, 0.5, 7.5, 3.5, 0.8, '#58a6ff', 'Reticle (Chrome/Quartz Mask)', '4× pattern, 6" x 6"')
# Objective lens elements (simplified)
y_lens = 3.0
for i, (label, dy, w_lens) in enumerate([
    ('Lens group 1\n(entry)',   0.0, 1.8),
    ('Pupil plane\n(aperture)', 1.2, 1.4),
    ('Lens group 2\n(field)',   2.4, 1.8),
    ('Pupil plane 2',           3.6, 1.4),
    ('Lens group 3\n(exit)',    4.8, 1.8),
]):
    yy = y_lens + 1.8 + dy
    lx = 2.25 - w_lens/4
    lens_patch = patches.Ellipse((2.25, yy + 0.3), w_lens, 0.4,
        linewidth=1.5, edgecolor='#bc8cff', facecolor='#1a0a2a', alpha=0.9)
    ax.add_patch(lens_patch)
    ax.text(4.0, yy + 0.3, label, color='#bc8cff', fontsize=6.5, va='center')

# Lens barrel annotation
barrel = patches.FancyBboxPatch((1.5, 3.0), 1.5, 5.5, boxstyle="round,pad=0.1",
    linewidth=2, edgecolor='#bc8cff', facecolor='none')
ax.add_patch(barrel)
ax.text(2.25, 2.7, 'Projection Lens Assembly\n(0.85 NA | 30 elements | 1.7m height)',
        ha='center', color='#bc8cff', fontsize=8, fontweight='bold')

# Wafer
comp_box(ax, 0.5, 1.0, 3.5, 0.8, '#57cc04', 'Silicon Wafer (300mm)', 'Photoresist coated | vacuum chuck')

# Beam arrows (light path)
beam_x = 2.25
for ya, yb in [(15.3, 14.5), (14.0, 13.2), (12.8, 12.0), (11.6, 10.8),
               (10.4, 9.6), (9.2, 8.7), (8.3, 7.5), (7.3, 6.5), (3.0, 1.8)]:
    # skip projection lens interior arrows
    pass
for ya, yb in [(14.3, 14.0), (13.0, 12.8), (11.8, 11.6), (10.6, 10.4),
               (9.4, 9.2), (8.5, 8.3), (7.3, 6.5)]:
    ax.annotate('', xy=(beam_x, yb), xytext=(beam_x, ya),
                arrowprops=dict(arrowstyle='->', color='#ff9500', lw=1.5), zorder=5)
ax.annotate('', xy=(beam_x, 1.8), xytext=(beam_x, 3.0),
            arrowprops=dict(arrowstyle='->', color='#ab63fa', lw=2.0), zorder=5)

ax.text(-0.8, 10.5, 'ILLUMINATION\nSYSTEM', color='#39d353', fontsize=8, 
        fontweight='bold', rotation=90, va='center')
ax.text(-0.8, 5.0, 'PROJECTION\nLENS', color='#bc8cff', fontsize=8,
        fontweight='bold', rotation=90, va='center')

# ============ RIGHT: Wafer stage detail ============
ax2 = axes[1]
ax2.set_facecolor('#0d1117')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 11)
ax2.axis('off')
ax2.set_title('Wafer Stage & Resist Process Detail', color='white', fontsize=10, fontweight='bold')

stage_components = [
    (1.0, 8.5, 8.0, 1.2, '#57cc04', 'Silicon Wafer (300 mm)', 'Positive CAR photoresist | PAB 110°C/60s'),
    (1.5, 7.0, 7.0, 1.0, '#2d5a27', 'Vacuum Chuck (Bernoulli)', 'Holds wafer flat | ±20 nm flatness'),
    (1.0, 5.8, 8.0, 0.8, '#1a3a1a', 'Fine Stage (Piezo)', 'XY range ±0.5mm | resolution 0.3 nm'),
    (1.0, 4.8, 8.0, 0.8, '#1a3a1a', 'Coarse Stage (Linear Motor)', 'Range ±150mm | velocity 500mm/s'),
    (0.5, 3.5, 9.0, 1.0, '#0a200a', 'Granite Base (vibration isolated)', 'Mass: 500 kg | air bearings'),
    (1.0, 2.0, 8.0, 1.0, '#0a150a', 'Laser Interferometer Grid', 'XY position | 0.08 nm resolution'),
]
for (x, y, w, h, fc, label, detail) in stage_components:
    r = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
        linewidth=1.5, edgecolor='#57cc04', facecolor=fc, alpha=0.85)
    ax2.add_patch(r)
    ax2.text(x+w/2, y+h/2+(0.1 if detail else 0), label,
             ha='center', va='center', color='white', fontsize=8.5, fontweight='bold')
    if detail:
        ax2.text(x+w/2, y+h/2-0.2, detail,
                 ha='center', va='center', color='#8b949e', fontsize=7)

# Resist process steps
process_steps = [
    (0.5, 9.9, '#eab308', 'RESIST PROCESS SEQUENCE'),
    (0.5, 9.5, '#c9d1d9', '1. Spin coat HMDS primer @ 3000 rpm'),
    (0.5, 9.15,'#c9d1d9', '2. Spin coat CAR photoresist @ 2000 rpm → 80 nm thick'),
    (0.5, 8.80,'#c9d1d9', '3. Pre-exposure bake (PAB) 110°C / 60 sec'),
    (0.5, 8.45,'#c9d1d9', '4. Expose: 193nm | dose = 25 mJ/cm² | focus ±50 nm'),
    (0.5, 8.10,'#c9d1d9', '5. Post-exposure bake (PEB) 120°C / 90 sec (acid diffusion)'),
    (0.5, 7.75,'#c9d1d9', '6. Develop TMAH 0.26N / 60 sec (positive tone)'),
    (0.5, 7.40,'#c9d1d9', '7. Inspect CD-SEM | target CD = 130 nm ± 5 nm'),
]
# skipping — moved below stage diagram
steps2 = [
    ('RESIST PROCESS',        '#eab308', True),
    ('1. Spin HMDS primer',   '#c9d1d9', False),
    ('2. Spin CAR resist 80nm','#c9d1d9', False),
    ('3. PAB 110°C / 60s',    '#c9d1d9', False),
    ('4. Expose 25mJ/cm²',    '#58a6ff', False),
    ('5. PEB 120°C / 90s',    '#c9d1d9', False),
    ('6. Develop TMAH 0.26N', '#c9d1d9', False),
    ('7. CD-SEM inspect',     '#39d353', False),
]
for i, (text, color, bold) in enumerate(steps2):
    y = 1.6 - i * 0.22
    ax2.text(0.6, y, ('  ' if not bold else '') + text, color=color, fontsize=8,
             fontweight='bold' if bold else 'normal')

# OPC note
opc_box = patches.FancyBboxPatch((0.5, -0.9), 9.0, 2.2, boxstyle="round,pad=0.1",
    linewidth=1.5, edgecolor='#f97316', facecolor='#1a0d00', alpha=0.9)
ax2.add_patch(opc_box)
ax2.text(5.0, 1.0, 'OPTICAL PROXIMITY CORRECTION (OPC)', color='#f97316',
         ha='center', fontsize=9, fontweight='bold')
ax2.text(5.0, 0.65, 'GDS polygons are modified BEFORE mask writing to compensate', 
         ha='center', color='#c9d1d9', fontsize=8)
ax2.text(5.0, 0.35, 'for diffraction effects. Corners get serifs, lines get biased.', 
         ha='center', color='#c9d1d9', fontsize=8)
ax2.text(5.0, 0.05, 'Rule-based OPC for 130nm node (model-based needed for sub-90nm)', 
         ha='center', color='#8b949e', fontsize=7.5)

plt.tight_layout()
plt.savefig('/home/saurabh-kumar123/Desktop/Desktop/express/duv_lithography/physical_design/optical_subsystem.png',
            dpi=140, bbox_inches='tight', facecolor='#0d1117')
print("Optical subsystem diagram saved!")
