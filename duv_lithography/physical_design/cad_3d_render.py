import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# ============================================================
# 3D CAD-style rendering of DUV Lithography Machine
# ============================================================

def box3d(ax, origin, size, color, alpha=0.6, edgecolor='white', lw=0.5):
    """Draw a 3D box (rectangular prism)."""
    ox, oy, oz = origin
    sx, sy, sz = size
    # 6 faces
    faces = [
        [[ox,oy,oz],[ox+sx,oy,oz],[ox+sx,oy+sy,oz],[ox,oy+sy,oz]],        # bottom
        [[ox,oy,oz+sz],[ox+sx,oy,oz+sz],[ox+sx,oy+sy,oz+sz],[ox,oy+sy,oz+sz]], # top
        [[ox,oy,oz],[ox+sx,oy,oz],[ox+sx,oy,oz+sz],[ox,oy,oz+sz]],         # front
        [[ox,oy+sy,oz],[ox+sx,oy+sy,oz],[ox+sx,oy+sy,oz+sz],[ox,oy+sy,oz+sz]],# back
        [[ox,oy,oz],[ox,oy+sy,oz],[ox,oy+sy,oz+sz],[ox,oy,oz+sz]],         # left
        [[ox+sx,oy,oz],[ox+sx,oy+sy,oz],[ox+sx,oy+sy,oz+sz],[ox+sx,oy,oz+sz]],# right
    ]
    poly = Poly3DCollection(faces, alpha=alpha, linewidths=lw,
                            edgecolors=edgecolor, facecolors=color)
    ax.add_collection3d(poly)

def cyl3d(ax, center, radius, height, color, alpha=0.6, n=20):
    """Draw a 3D cylinder."""
    cx, cy, cz = center
    theta = np.linspace(0, 2*np.pi, n)
    x = cx + radius * np.cos(theta)
    y = cy + radius * np.sin(theta)
    z_bot = np.full_like(theta, cz)
    z_top = np.full_like(theta, cz + height)
    # Side
    for i in range(n-1):
        verts = [[x[i],y[i],z_bot[i]],[x[i+1],y[i+1],z_bot[i+1]],
                 [x[i+1],y[i+1],z_top[i+1]],[x[i],y[i],z_top[i]]]
        p = Poly3DCollection([verts], alpha=alpha, facecolors=color, 
                              edgecolors='white', linewidths=0.3)
        ax.add_collection3d(p)
    # Top/bottom caps
    for zz in [cz, cz+height]:
        cap = [[x[i], y[i], zz] for i in range(n-1)]
        p = Poly3DCollection([cap], alpha=alpha+0.1, facecolors=color, 
                              edgecolors='white', linewidths=0.3)
        ax.add_collection3d(p)

fig = plt.figure(figsize=(18, 12), facecolor='#0d1117')
ax  = fig.add_subplot(111, projection='3d', facecolor='#0d1117')

# ============================================================
# Machine components layout (all units in cm for real scale)
# Machine total size: 2.4m W × 1.6m D × 2.1m H
# ============================================================

# 1. GRANITE BASE — massive vibration-isolated block
box3d(ax, (0,0,0),    (24,16,4),  '#555566', alpha=0.7, edgecolor='#aaaacc')

# 2. WAFER STAGE — sits on granite
box3d(ax, (6,5,4),    (12,6,3),   '#2d5a27', alpha=0.8,  edgecolor='#57cc04')
# Wafer (circle approximated as thin box)
box3d(ax, (8,6.5,7),  (8,3,0.3),  '#cccccc', alpha=0.9,  edgecolor='#888888')

# 3. PROJECTION LENS BARREL — tall cylinder above wafer stage
cyl3d(ax, (11, 8, 7), 2.5, 14, '#1a0a2a', alpha=0.7, n=30)
# Lens housing rings
for zh in [8, 11, 14, 17, 19]:
    cyl3d(ax, (11, 8, zh), 2.7, 0.5, '#4a2080', alpha=0.9, n=30)

# 4. RETICLE STAGE — above projection lens
box3d(ax, (7, 4, 21), (8, 8, 2.5),  '#003366', alpha=0.8, edgecolor='#58a6ff')
# Reticle plate
box3d(ax, (8, 5.5, 23.5), (6, 5, 0.3), '#ccccff', alpha=0.9, edgecolor='#aaaaff')

# 5. ILLUMINATION COLUMN — above reticle
box3d(ax, (8.5, 5.5, 24), (5, 5, 6),  '#003322', alpha=0.7, edgecolor='#39d353')
# Fly-eye lens block
box3d(ax, (9, 6, 27),   (4, 4, 1.5), '#004400', alpha=0.85, edgecolor='#57cc04')

# 6. LASER HEAD — side mounted, connects to illumination via beam pipe
box3d(ax, (20, 6, 24), (4, 4, 4),   '#3d0000', alpha=0.8, edgecolor='#ff6b35')
# Power supply
box3d(ax, (20, 6, 19), (4, 4, 4.5), '#2d1500', alpha=0.7, edgecolor='#ff8c00')
# Beam pipe (laser → illuminator)
box3d(ax, (13, 7.5, 25.5), (7, 1, 1), '#1a3300', alpha=0.8, edgecolor='#39d353')

# 7. CONTROL CABINET — right side
box3d(ax, (20, 1, 0),  (4, 4, 18),  '#1a1500', alpha=0.7, edgecolor='#f97316')
# Control panels (screens)
box3d(ax, (20.1, 1.5, 10), (3.8, 0.3, 5), '#000066', alpha=0.9, edgecolor='#58a6ff')

# 8. COAT/DEV TRACK — left side
box3d(ax, (-6, 0, 0),  (5.5, 16, 12), '#151500', alpha=0.6, edgecolor='#eab308')

# 9. ENVIRONMENTAL ENCLOSURE (ghost outline)
enclosure_verts = [
    [(-6,0,0),  (24,0,0),  (24,16,0),  (-6,16,0)],  # floor
    [(-6,0,32), (24,0,32), (24,16,32), (-6,16,32)],  # ceiling
    [(-6,0,0),  (24,0,0),  (24,0,32),  (-6,0,32)],   # front wall
    [(-6,16,0), (24,16,0), (24,16,32), (-6,16,32)],  # back wall
]
for face in enclosure_verts:
    p = Poly3DCollection([face], alpha=0.04, facecolors='#58a6ff', 
                          edgecolors='#58a6ff', linewidths=0.8, linestyles='--')
    ax.add_collection3d(p)

# Dimension annotations
ax.text(12, -1, 0,  '2.4 m', color='#ffd700', fontsize=9, ha='center')
ax.text(25, 8,  2,  '1.6 m', color='#ffd700', fontsize=9)
ax.text(25, 0,  16, '2.1 m', color='#ffd700', fontsize=9)

# Component labels
label_data = [
    (12, 8,  2.5,  'Wafer Stage\n(300mm Si)',   '#57cc04'),
    (12, 8,  15,   'Projection Lens\n(NA=0.85)', '#bc8cff'),
    (12, 8,  22.5, 'Reticle Stage\n(6" mask)',   '#58a6ff'),
    (11, 8,  28,   'Illumination\nColumn',        '#39d353'),
    (22, 8,  26,   'ArF Laser\n193nm 40W',        '#ff6b35'),
    (22, 3,  9,    'Control\nCabinet',            '#f97316'),
    (-3.5, 8,6,    'Coat/Dev\nTrack',             '#eab308'),
]
for (x, y, z, lbl, c) in label_data:
    ax.text(x, y, z, lbl, color=c, fontsize=8, fontweight='bold',
            ha='center', va='bottom', zorder=10)

# View angle
ax.view_init(elev=25, azim=-50)

ax.set_xlim(-6, 26)
ax.set_ylim(-2, 18)
ax.set_zlim(0, 34)
ax.set_xlabel('X (cm)', color='gray', fontsize=8, labelpad=5)
ax.set_ylabel('Y (cm)', color='gray', fontsize=8, labelpad=5)
ax.set_zlabel('Z (cm)', color='gray', fontsize=8, labelpad=5)
ax.tick_params(colors='gray', labelsize=7)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('#30363d')
ax.yaxis.pane.set_edgecolor('#30363d')
ax.zaxis.pane.set_edgecolor('#30363d')

ax.set_title('193nm DUV ArF Lithography Machine — 3D CAD Render\n'
             '2.4m × 1.6m × 2.1m | 30,000 kg | Targeting SKY130 130nm Node',
             color='white', fontsize=13, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('/home/saurabh-kumar123/Desktop/Desktop/express/duv_lithography/physical_design/cad_3d_isometric.png',
            dpi=150, bbox_inches='tight', facecolor='#0d1117')
print("3D CAD isometric render saved!")
