import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import numpy as np

fig = plt.figure(figsize=(22, 16), facecolor='#0d1117')
fig.suptitle('193nm DUV Lithography Machine — Engineering Drawing (Orthographic Projections)\n'
             'Third-Angle Projection | All dimensions in mm | Scale 1:25',
             color='white', fontsize=13, fontweight='bold', y=0.99)

# Three views: Front (large), Side, Top
ax_front = fig.add_axes([0.03, 0.08, 0.50, 0.86], facecolor='#0a0e1a')
ax_side  = fig.add_axes([0.55, 0.44, 0.22, 0.50], facecolor='#0a0e1a')
ax_top   = fig.add_axes([0.55, 0.08, 0.22, 0.32], facecolor='#0a0e1a')
ax_bom   = fig.add_axes([0.79, 0.08, 0.20, 0.86], facecolor='#0a0e1a')

# ============================================================
# SHARED COLORS
COL_SIL  = '#aaaaaa'  # silver (general structure)
COL_LENS = '#9966cc'  # purple (optics)
COL_LASR = '#ff4400'  # red (laser)
COL_STG  = '#228800'  # green (stages)
COL_CTRL = '#cc8800'  # amber (control)
COL_ENV  = '#004488'  # blue (enclosure)
COL_DIM  = '#ffd700'  # yellow (dimensions)
COL_CENT = '#ff6666'  # centerlines

def dim_arrow(ax, x1, y1, x2, y2, label, offset=(0,0), color='#ffd700', fontsize=7.5):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.2))
    mx = (x1+x2)/2 + offset[0]
    my = (y1+y2)/2 + offset[1]
    ax.text(mx, my, label, color=color, fontsize=fontsize, ha='center', va='center',
            bbox=dict(facecolor='#0a0e1a', edgecolor='none', pad=1))

def rect(ax, x, y, w, h, fc, ec='white', lw=0.8, alpha=0.85, label='', fs=7):
    r = patches.Rectangle((x,y), w, h, linewidth=lw, edgecolor=ec,
                           facecolor=fc, alpha=alpha)
    ax.add_patch(r)
    if label:
        ax.text(x+w/2, y+h/2, label, ha='center', va='center',
                color='white', fontsize=fs, fontweight='bold')

def centerline(ax, x1, y1, x2, y2):
    ax.plot([x1,x2],[y1,y2], color=COL_CENT, linewidth=0.6,
            linestyle=(0,(5,3,1,3)), alpha=0.7)

# ============================================================
# FRONT VIEW (looking from Y axis — shows X and Z)
# Scale: 1 unit = 1 cm → real machine 240 cm W × 210 cm H
ax = ax_front
ax.set_xlim(-10, 250)
ax.set_ylim(-5, 220)
ax.set_aspect('equal')
ax.tick_params(colors='gray', labelsize=7)
for sp in ax.spines.values(): sp.set_color('#30363d')

ax.set_title('FRONT VIEW', color='white', fontsize=10, fontweight='bold', pad=5)
ax.set_xlabel('Width (cm) →', color='gray', fontsize=7)
ax.set_ylabel('Height (cm) →', color='gray', fontsize=7)

# Granite base
rect(ax,  0,  0, 240, 40, '#444455', '#aaaacc', label='GRANITE BASE (500 kg)\nVibration Isolation Pads')
# Laser power supply
rect(ax,  0, 40,  50, 60, '#2d1500', COL_LASR, label='Laser PSU')
# Coat/dev track
rect(ax,  0,100,  55,110, '#151500', '#eab308', label='COAT/DEV\nTRACK')
# Wafer stage
rect(ax, 55, 40, 130, 30, '#1a3300', COL_STG, label='WAFER STAGE (XY piezo | 300mm chuck)')
# Projection lens barrel (tall)
rect(ax, 95, 70,  50,130, '#1a0a2a', COL_LENS, label='PROJECTION LENS\nASSEMBLY\nNA=0.85 | 30 elements\nFused Silica + CaF₂')
# Lens rings (decorative)
for rh in [80, 96, 112, 128, 148, 167]:
    rect(ax, 93, rh, 54, 5, '#2d1a44', '#9955cc', alpha=0.9)
# Reticle stage
rect(ax, 75,200,  90, 10, '#001a33', COL_ENV, label='RETICLE STAGE (4:1 mask, 6" quartz)')
# Illumination column
rect(ax, 85,170,  70, 30, '#001a0a', '#39d353', label='ILLUMINATION COLUMN\n(Köhler | σ=0.7)')
# Laser head
rect(ax,185, 40,  55, 55, '#2a0000', COL_LASR, label='ArF EXCIMER\nLASER HEAD\n193nm | 40W\n6kHz rep rate')
# Beam path (dashed line)
ax.plot([185, 155], [67.5, 67.5], color='#ff6600', linewidth=1.5, 
        linestyle='--', label='193nm beam')
ax.plot([155, 120], [67.5, 185], color='#ff6600', linewidth=1.5, linestyle='--')
# Control cabinet
rect(ax,185,100,  55,110, '#1a1500', COL_CTRL, label='CONTROL\nCABINET\n(Real-time OS\n+ SPC)')

# Centerlines
centerline(ax, 120, 0, 120, 215)   # machine vertical center
centerline(ax, 0, 55, 250, 55)     # wafer plane

# Dimension arrows
dim_arrow(ax, 0, -3, 240, -3, '2400 mm', (0, -1.5))
dim_arrow(ax, -7, 0, -7, 210, '2100 mm', (-6, 0))
dim_arrow(ax, -5, 0, -5, 40, '400 mm\n(base)', (-4, 0))
dim_arrow(ax, 95, 215, 145, 215, '500 mm\n(lens ø)', (0, 4))
dim_arrow(ax, 245, 70, 245, 200, '1300 mm\n(lens H)', (6, 0))

# Label beam
ax.text(170, 72, '193nm beam', color='#ff6600', fontsize=7, style='italic')

# Grid (light)
ax.set_xticks(range(0, 250, 20))
ax.set_yticks(range(0, 220, 20))
ax.grid(True, color='#1a1a2a', linewidth=0.4, alpha=0.6)

# ============================================================
# SIDE VIEW (looking from X axis — shows Y and Z)
ax = ax_side
ax.set_xlim(-5, 175)
ax.set_ylim(-5, 220)
ax.set_aspect('equal')
ax.tick_params(colors='gray', labelsize=6)
for sp in ax.spines.values(): sp.set_color('#30363d')
ax.set_title('SIDE VIEW', color='white', fontsize=9, fontweight='bold', pad=4)
ax.set_xlabel('Depth (cm)', color='gray', fontsize=7)
ax.set_ylabel('Height (cm)', color='gray', fontsize=7)

rect(ax,  0,  0, 160, 40, '#444455', '#aaaacc')             # granite
rect(ax, 15, 40, 130, 30, '#1a3300', COL_STG)                # wafer stage
rect(ax, 55, 70,  50,130, '#1a0a2a', COL_LENS)               # lens
rect(ax, 45,200,  70, 10, '#001a33', COL_ENV)                 # reticle
rect(ax, 50,170,  60, 30, '#001a0a', '#39d353')               # illuminator
rect(ax,  0, 40,  14, 60, '#2a0000', COL_LASR)               # laser

dim_arrow(ax, -3, 0, -3, 210, '2100 mm', (-6, 0))
dim_arrow(ax, 0, -3, 160, -3, '1600 mm depth', (0, -2))
ax.grid(True, color='#1a1a2a', linewidth=0.4, alpha=0.6)
centerline(ax, 80, 0, 80, 215)

# ============================================================
# TOP VIEW (looking down Z axis — shows X and Y)
ax = ax_top
ax.set_xlim(-10, 250)
ax.set_ylim(-5, 170)
ax.set_aspect('equal')
ax.tick_params(colors='gray', labelsize=6)
for sp in ax.spines.values(): sp.set_color('#30363d')
ax.set_title('TOP VIEW', color='white', fontsize=9, fontweight='bold', pad=4)
ax.set_xlabel('Width (cm)', color='gray', fontsize=7)
ax.set_ylabel('Depth (cm)', color='gray', fontsize=7)

rect(ax,  0,  0, 240, 160, '#444455', '#aaaacc')   # granite footprint
rect(ax, 55, 15, 130, 130, '#1a3300', COL_STG, label='Wafer Stage')
# Wafer circle
wafer_circ = plt.Circle((120, 80), 45, color='#cccccc', alpha=0.8, 
                          linewidth=1.5, fill=True)
ax.add_patch(wafer_circ)
ax.text(120, 80, '300mm\nWafer', ha='center', va='center', color='black', fontsize=7, fontweight='bold')
rect(ax, 185, 30,  55, 100, '#2a0000', COL_LASR, label='Laser\n+ PSU')
rect(ax,  0,  0,  55, 155, '#151500', '#eab308', label='Track')
# Lens barrel (circle from top)
lens_circ = plt.Circle((120, 80), 25, fill=False, edgecolor=COL_LENS, 
                         linewidth=2, linestyle='--')
ax.add_patch(lens_circ)
ax.text(120, 125, 'Lens ø500mm', ha='center', color=COL_LENS, fontsize=6)

dim_arrow(ax, 0, -3, 240, -3, '2400 mm', (0,-2))
dim_arrow(ax, -7, 0, -7, 160, '1600 mm', (-4,0))
ax.grid(True, color='#1a1a2a', linewidth=0.4, alpha=0.6)
centerline(ax, 120, 0, 120, 165)
centerline(ax, 0, 80, 245, 80)

# ============================================================
# BOM (Bill of Materials)
ax = ax_bom
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('BILL OF MATERIALS', color='white', fontsize=9, fontweight='bold')

bom = [
    ('1', 'ArF Excimer Laser',     '193nm 40W 6kHz', 'Cymer/Gigaphoton'),
    ('2', 'Beam Delivery Module',  'Expander+attenuator', 'OEM'),
    ('3', 'Fly-Eye Lens (ilum.)',  'Fused silica array', 'Zeiss'),
    ('4', 'Condenser Optics',      'σ=0.7 setting', 'Zeiss'),
    ('5', 'Reticle Stage',         '6" quartz ±0.5nm', 'Zygo'),
    ('6', 'Projection Lens',       'NA=0.85 30-elem', 'Zeiss/Nikon'),
    ('7', 'Wafer Stage',           '300mm XY piezo', 'ASML/Canon'),
    ('8', 'Granite Base',          '500 kg air-bearing', 'Custom'),
    ('9', 'Control Computer',      'Real-time Linux', 'Custom'),
    ('10','Env. Control Unit',     'T±0.01°C, N2 purge', 'Custom'),
    ('11','Coat/Dev Track',        'Spin coat + TMAH dev', 'TEL/SST'),
    ('12','Alignment System',      'TTL off-axis laser', 'ASML'),
    ('13','Interferometer grid',   'XY 0.08nm resolution', 'Zygo'),
    ('14','PSU + chiller',         '3-phase 400V 30kW', 'Custom'),
]

ax.text(5, 9.7, 'Item  Component               Spec', color='#58a6ff', 
        fontsize=7, ha='center', fontweight='bold', family='monospace')
ax.axhline(9.55, color='#30363d', linewidth=0.8)

for i, (num, name, spec, mfg) in enumerate(bom):
    y = 9.3 - i * 0.60
    ax.text(0.2, y, num, color='#ffd700', fontsize=6.5, fontweight='bold')
    ax.text(0.8, y, name, color='white', fontsize=6.5)
    ax.text(0.8, y-0.22, spec, color='#8b949e', fontsize=5.8)
    if i % 2 == 0:
        rect(ax, 0, y-0.28, 10, 0.55, '#161b22', 'none', alpha=0.5)

# Machine stats
ax.axhline(0.9, color='#30363d', linewidth=0.8)
stats = [
    ('Footprint', '2.4m × 1.6m'),
    ('Height',    '2.1m'),
    ('Weight',    '~30,000 kg'),
    ('Power',     '30 kW (3-phase)'),
    ('Cooling',   'DI water + chiller'),
    ('Class',     'ISO Class 1 cleanroom'),
]
for i, (k, v) in enumerate(stats):
    y = 0.75 - i * 0.14
    ax.text(0.5, y, f'{k}: {v}', color='#c9d1d9', fontsize=6.5)

plt.savefig('/home/saurabh-kumar123/Desktop/Desktop/express/duv_lithography/physical_design/cad_ortho_drawings.png',
            dpi=140, bbox_inches='tight', facecolor='#0d1117')
print("Orthographic engineering drawings saved!")
