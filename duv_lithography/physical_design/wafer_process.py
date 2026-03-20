import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(20, 10), facecolor='#0d1117')
fig.suptitle('DUV Wafer Process — Layer Stack Formation & Step-and-Scan Operation',
             color='white', fontsize=13, fontweight='bold')

# ============ LEFT: Wafer cross-section process steps ============
ax = axes[0]
ax.set_facecolor('#0d1117')
ax.set_xlim(0, 10)
ax.set_ylim(-1, 14)
ax.axis('off')
ax.set_title('Silicon Wafer Cross-Section — Layer Formation Sequence', 
             color='white', fontsize=10, fontweight='bold')

steps = [
    # (y, height, layers, title)
    (0.0, 1.5, [('#aaaaaa', 4.0, 'Si substrate (300mm, p-type)')], 
     'Step 1: Silicon Wafer'),
    (2.0, 1.5, [
        ('#aaaaaa', 4.0, 'Si substrate'),
        ('#4444ff', 0.4, 'SiO₂ gate oxide (2 nm, thermal)')], 
     'Step 2: Gate Oxide'),
    (4.0, 1.5, [
        ('#aaaaaa', 4.0, 'Si substrate'),
        ('#4444ff', 0.4, 'SiO₂'),
        ('#888800', 0.5, 'Poly-Si gate (130 nm, CVD)')], 
     'Step 3: Poly-Si Deposition'),
    (6.0, 1.8, [
        ('#aaaaaa', 4.0, 'Si substrate'),
        ('#4444ff', 0.4, 'SiO₂'),
        ('#888800', 0.5, 'Poly-Si'),
        ('#cc6600', 0.35, 'Photoresist (CAR, 80 nm)')], 
     'Step 4: Resist Coat → UV Expose → Develop'),
    (8.2, 1.5, [
        ('#aaaaaa', 4.0, 'Si substrate'),
        ('#4444ff', 0.4, 'SiO₂'),
        ('#888800', 0.5, 'Poly-Si (patterned gate) ← 130 nm CD')], 
     'Step 5: Etch (RIE) → Strip Resist'),
    (10.5, 1.5, [
        ('#aaaaaa', 4.0, 'Si substrate'),
        ('#4444ff', 0.4, 'SiO₂'),
        ('#888800', 0.5, 'Poly-Si gate'),
        ('#005500', 0.6, 'n⁺/p⁺ S/D implant → anneal'),
        ('#333366', 0.5, 'Spacer (Si₃N₄)')], 
     'Step 6: Implant + Anneal'),
]

for (y_base, row_h, layer_list, title) in steps:
    # Draw sub-layers
    y_cur = y_base
    for (color, rel_h, label) in layer_list:
        scale = row_h / sum(l[1] for l in layer_list)
        lh = rel_h * scale * 0.7
        rect = patches.FancyBboxPatch((1.0, y_cur), 6.0, lh,
            boxstyle="square,pad=0", linewidth=1,
            edgecolor='#30363d', facecolor=color, alpha=0.85)
        ax.add_patch(rect)
        ax.text(4.0, y_cur + lh/2, label, ha='center', va='center',
                color='white', fontsize=7, fontweight='bold')
        y_cur += lh

    # Title on right
    ax.text(7.5, y_base + row_h*0.35, title, color='#58a6ff', fontsize=8.5,
            fontweight='bold', va='center')
    # Step divider
    ax.axhline(y=y_base - 0.1, xmin=0.05, xmax=0.95, color='#30363d', 
               linewidth=0.8, linestyle='--')

# Arrows between steps
for y_arr in [1.6, 3.6, 5.6, 7.8, 10.1]:
    ax.annotate('', xy=(4.0, y_arr-0.05), xytext=(4.0, y_arr-0.35),
                arrowprops=dict(arrowstyle='->', color='#57cc04', lw=1.5))

# ============ RIGHT: Step-and-Scan map ============
ax2 = axes[1]
ax2.set_facecolor('#0d1117')
ax2.set_aspect('equal')
ax2.set_xlim(-1, 18)
ax2.set_ylim(-1, 18)

# Wafer circle
wafer = plt.Circle((8, 8), 7.5, color='#333', linewidth=2, 
                    fill=True, facecolor='#1a1a2a', edgecolor='#888')
ax2.add_patch(wafer)

# Die/shot grid
shot_w = 2.0
shot_h = 2.0
dx, dy = shot_w + 0.05, shot_h + 0.05
exposed_count = 0
colors_exp = ['#00b4d8', '#0077b6', '#023e8a']
for ix in range(7):
    for iy in range(7):
        x = 8 - 3.5*dx + ix*dx
        y = 8 - 3.5*dy + iy*dy
        # Check if die is within wafer circle
        dist = np.sqrt((x + shot_w/2 - 8)**2 + (y + shot_h/2 - 8)**2)
        if dist < 7.0:
            c = colors_exp[exposed_count % 3]
            shot = patches.Rectangle((x, y), shot_w, shot_h,
                linewidth=0.8, edgecolor='#58a6ff', facecolor=c, alpha=0.6)
            ax2.add_patch(shot)
            ax2.text(x + shot_w/2, y + shot_h/2, f'({ix},{iy})',
                    ha='center', va='center', color='white', fontsize=5.5)
            exposed_count += 1

# Scan direction arrows
ax2.annotate('', xy=(15.5, 8), xytext=(14.5, 8),
            arrowprops=dict(arrowstyle='->', color='#ffd700', lw=2))
ax2.annotate('', xy=(8, 15.5), xytext=(8, 14.5),
            arrowprops=dict(arrowstyle='->', color='#f97316', lw=2))
ax2.text(15.6, 8.2, 'X scan\n(reticle)', color='#ffd700', fontsize=8)
ax2.text(8.2, 15.7, 'Y step', color='#f97316', fontsize=8)

# Spec callouts
info = [
    (0.2, 16.5, '#c9d1d9', f'Wafer: 300 mm silicon'),
    (0.2, 16.0, '#c9d1d9', f'Die size: {shot_w}×{shot_h} cm'),
    (0.2, 15.5, '#57cc04', f'Dies per wafer: {exposed_count}'),
    (0.2, 15.0, '#c9d1d9', 'Throughput: ~150 wafers/hr'),
    (0.2, 14.5, '#c9d1d9', 'Scan speed: 500 mm/s (reticle)'),
    (0.2, 14.0, '#c9d1d9', 'Step speed: 1000 mm/s (wafer)'),
    (0.2, 13.5, '#58a6ff', 'Overlay: < 5 nm (3σ)'),
    (0.2, 13.0, '#c9d1d9', 'Focus: ±50 nm (autofocus)'),
]
for (x, y, c, t) in info:
    ax2.text(x, y, t, color=c, fontsize=8)

ax2.set_title('Step-and-Scan Operation — 300mm Wafer', color='white', fontsize=10, fontweight='bold')
ax2.set_xlabel('X position (cm)', color='gray', fontsize=8)
ax2.set_ylabel('Y position (cm)', color='gray', fontsize=8)
ax2.tick_params(colors='gray', labelsize=7)
for sp in ax2.spines.values():
    sp.set_color('#30363d')

plt.tight_layout()
plt.savefig('/home/saurabh-kumar123/Desktop/Desktop/express/duv_lithography/physical_design/wafer_process.png',
            dpi=140, bbox_inches='tight', facecolor='#0d1117')
print("Wafer process diagram saved!")
