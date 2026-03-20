import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(20, 13), facecolor='#0d1117')
ax.set_facecolor('#0d1117')
ax.set_xlim(0, 20)
ax.set_ylim(0, 13)
ax.axis('off')

ax.set_title('193 nm ArF DUV Lithography Machine — Full System Architecture\n'
             'Targeting SKY130 130nm Node | NA=0.85 | 4:1 Reduction Stepper',
             color='white', fontsize=14, fontweight='bold', pad=12)

def box(ax, x, y, w, h, fc, ec, label, sublabel='', fontsize=9):
    r = patches.FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0.05",
        linewidth=2, edgecolor=ec, facecolor=fc, alpha=0.88, zorder=3)
    ax.add_patch(r)
    ax.text(x+w/2, y+h/2 + (0.1 if sublabel else 0), label,
            ha='center', va='center', color='white', fontsize=fontsize,
            fontweight='bold', zorder=4)
    if sublabel:
        ax.text(x+w/2, y+h/2 - 0.2, sublabel,
                ha='center', va='center', color='#8b949e', fontsize=7, zorder=4)

def arrow(ax, x1, y1, x2, y2, color='#58a6ff', label='', lw=2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw),
                zorder=5)
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx+0.05, my+0.08, label, color=color, fontsize=6.5, ha='center', zorder=6)

# ============================================================
# SUBSYSTEMS (left to right, top to bottom as in real machine)
# ============================================================

# 1. ArF Laser
box(ax, 0.3, 9.5, 2.8, 2.0, '#1a0a00', '#ff6b35',
    'ArF Excimer\nLaser', '193 nm | 40 W\n6 kHz repetition', fontsize=8)

# 2. Beam Delivery / Attenuator
box(ax, 3.5, 9.5, 2.5, 2.0, '#1a1a00', '#ffd700',
    'Beam Delivery\nSystem', 'Attenuator + expander\nHomogenizer', fontsize=8)
arrow(ax, 3.1, 10.5, 3.5, 10.5, '#ff6b35', '193nm beam')

# 3. Illuminator / Köhler
box(ax, 6.4, 9.5, 2.5, 2.0, '#001a0a', '#39d353',
    'Illumination\nOptics', 'Köhler illumination\nσ=0.7 (partial coh.)', fontsize=8)
arrow(ax, 6.0, 10.5, 6.4, 10.5, '#ffd700', 'conditioned')

# 4. Reticle Stage
box(ax, 9.3, 9.0, 3.0, 2.5, '#001a1a', '#58a6ff',
    'Reticle (Photomask)\nStage', '6" quartz mask\n4× pattern | ±0.5 nm\npositioning', fontsize=8)
arrow(ax, 8.9, 10.5, 9.3, 10.5, '#39d353', 'illuminated')

# 4b. Reticle detail
box(ax, 9.5, 7.5, 2.5, 1.2, '#00101a', '#58a6ff',
    'Chrome on Quartz\nMask (4:1 reduction)', '130nm features → 520nm on mask', fontsize=7)
arrow(ax, 10.8, 9.0, 10.8, 8.7, '#58a6ff', '')

# 5. Projection Lens
box(ax, 9.3, 4.8, 3.0, 2.2, '#1a001a', '#bc8cff',
    'Projection Lens\nAssembly (PO)', 'NA=0.85 | 30 elements\nFused silica + CaF₂\nMotorized aberr. control', fontsize=8)
arrow(ax, 10.8, 7.5, 10.8, 7.0, '#58a6ff', '')
arrow(ax, 10.8, 6.3, 10.8, 7.0, '#bc8cff', '4:1 reduction', )
# correction: arrow down from reticle to lens
ax.annotate('', xy=(10.8, 7.0), xytext=(10.8, 7.5),
            arrowprops=dict(arrowstyle='->', color='#58a6ff', lw=2), zorder=5)

# 6. Wafer Stage
box(ax, 8.5, 1.5, 4.5, 2.8, '#0a1a00', '#57cc04',
    'Wafer Stage', '300mm Si wafer\nXY: ±0.3 nm precision\nPiezo + linear motor\nVacuum chuck', fontsize=8)

# Arrow from lens to wafer
ax.annotate('', xy=(10.8, 4.3), xytext=(10.8, 4.8),
            arrowprops=dict(arrowstyle='->', color='#bc8cff', lw=2.5), zorder=5)
ax.text(11.0, 4.55, 'aerial image\n(shrunk 4×)', color='#bc8cff', fontsize=7)

# 7. Alignment System
box(ax, 14.0, 7.5, 3.5, 2.0, '#1a0a1a', '#e879f9',
    'Alignment &\nMetrology System', 'Off-axis laser align\nTTL + interferometer\n<1nm overlay', fontsize=8)

# 8. Environmental Control
box(ax, 14.0, 4.5, 3.5, 2.5, '#001520', '#06b6d4',
    'Environmental\nControl', 'Temperature: ±0.01°C\nVibration isolation\nNitrogen purge\nHumidity < 1%', fontsize=8)

# 9. Control Computer
box(ax, 14.0, 1.5, 3.5, 2.5, '#150a00', '#f97316',
    'Control System\n(Real-time OS)', 'GDS → Mask data prep\nStepper control\nFocus/dose recipe\nLog & SPC', fontsize=8)

# 10. Resist Coat/Dev Track (connected)
box(ax, 0.3, 1.5, 3.5, 2.8, '#151500', '#eab308',
    'Coat/Develop Track\n(inline)', 'Spin coat photoresist\nPAB 110°C / 60s\nDevelop TMAH 0.26N\nPEB + rinse', fontsize=8)

# Arrow connections
arrow(ax, 14.0, 3.0, 13.0, 3.0, '#f97316', 'stage cmd')
arrow(ax, 14.0, 6.5, 12.8, 6.5, '#e879f9', 'align feedback')
arrow(ax, 3.8, 3.0, 8.5, 3.0, '#eab308', 'coated wafer in')
arrow(ax, 8.5, 2.0, 3.8, 2.0, '#57cc04', 'exposed wafer out')

# Light path annotations
ax.text(10.4, 8.9, 'IMAGE\nPLANE', color='#58a6ff', fontsize=7, ha='center', style='italic')
ax.text(10.4, 6.25, 'OBJECT\nPLANE', color='#bc8cff', fontsize=7, ha='center', style='italic')

# Key specs box
spec_box = patches.FancyBboxPatch((0.3, 5.5), 8.2, 3.5,
    boxstyle="round,pad=0.1",
    linewidth=1.5, edgecolor='#30363d', facecolor='#161b22', alpha=0.9, zorder=2)
ax.add_patch(spec_box)
specs = [
    ('Wavelength',     '193 nm (ArF)'),
    ('Node target',    '130 nm (SKY130)'),
    ('Resolution limit','k₁·λ/NA = 0.4×193/0.85 = 91 nm'),
    ('Numerical aperture','NA = 0.85'),
    ('Reduction ratio', '4:1'),
    ('Wafer size',     '300 mm'),
    ('Throughput',     '~150 wafers/hr'),
    ('Overlay',        '< 5 nm 3σ'),
    ('Depth of focus', '±λ/(2·NA²) = ±134 nm'),
    ('Laser power',    '40 W @ 6 kHz'),
    ('Resist', 'Chemically amplified (CAR)'),
]
ax.text(0.5, 8.9, 'KEY SPECIFICATIONS', color='#58a6ff', fontsize=9, fontweight='bold')
for i, (k, v) in enumerate(specs):
    y = 8.6 - i * 0.28
    ax.text(0.5, y, f'{k}:', color='#8b949e', fontsize=7.2)
    ax.text(4.2, y, v, color='white', fontsize=7.2)

plt.tight_layout()
plt.savefig('/home/saurabh-kumar123/Desktop/Desktop/express/duv_lithography/physical_design/machine_overview.png',
            dpi=140, bbox_inches='tight', facecolor='#0d1117')
print("Machine overview saved!")
