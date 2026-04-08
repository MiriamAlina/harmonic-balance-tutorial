import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def draw_undamped_linear_system():
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    ax.axis('off')

    # wall
    for y in np.linspace(1.0, 2.75, 9):
        ax.plot([0.0, 0.25], [y, y + 0.25], color='gray', lw=1.0)
    ax.plot([0.25, 0.25], [1.0, 3.0], color='black', lw=1.5)

    # ground
    for x in np.linspace(0.25, 4.7, 18):
        ax.plot([x, x - 0.25], [1.0, 0.75], color='gray', lw=0.8)
    ax.plot([0.25, 4.8], [1.0, 1.0], color='black', lw=1.5)

    # spring (zigzag)
    x_start, x_end, y_spring, n_coils = 0.25, 1.7, 1.8, 5
    xs = np.linspace(x_start, x_end, n_coils * 2 + 2)
    ys = np.zeros_like(xs)
    ys[0], ys[-1] = y_spring, y_spring
    for i in range(1, len(xs) - 1):
        ys[i] = y_spring + (0.2 if i % 2 == 1 else -0.2)
    ax.plot(xs, ys, color='#008b9a', lw=2.0)
    ax.text((x_start + x_end) / 2, y_spring + 0.25, r'$c$', ha='center',
            va='bottom', fontsize=14, color='#008b9a')

    # mass block
    mass_x, mass_y, mass_w, mass_h = 1.75, 1.3, 1.5, 1.0
    rect = mpatches.FancyBboxPatch((mass_x, mass_y), mass_w, mass_h,
                                   boxstyle='round,pad=0.05', linewidth=1.5,
                                   edgecolor='black', facecolor='#a8dadc')
    ax.add_patch(rect)
    ax.text(mass_x + mass_w / 2, mass_y + mass_h / 2, r'$m$', ha='center',
            va='center', fontsize=14)

    # force arrow
    ax.annotate('', xy=(mass_x + mass_w + 0.8, mass_y + mass_h / 2),
                xytext=(mass_x + mass_w, mass_y + mass_h / 2),
                arrowprops=dict(arrowstyle='->', color='#e63946', lw=2.0))
    ax.text(mass_x + mass_w + 0.9, mass_y + mass_h / 2, r'$f_{\mathrm{ex}}$',
            ha='left', va='center', fontsize=14, color='#e63946')

    # displacement arrow
    arrow_y = mass_y + 1.5
    ax.annotate('', xy=(mass_x + mass_w * 0.8, arrow_y),
                xytext=(mass_x + mass_w * 0.2, arrow_y),
                arrowprops=dict(arrowstyle='->', color='dimgray', lw=1.5))
    ax.text(mass_x + mass_w / 2, arrow_y - 0.12, r'$q$', ha='center', va='top',
            fontsize=14, color='dimgray')

    # rollers
    for rx in [mass_x + 0.4, mass_x + 1.1]:
        ax.add_patch(plt.Circle((rx, 1.13), 0.11, color='gray', zorder=3))

    plt.show()


def draw_damped_linear_system():
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    ax.axis('off')

    # wall
    for y in np.linspace(1.0, 2.75, 9):
        ax.plot([0.0, 0.25], [y, y + 0.25], color='gray', lw=1.0)
    ax.plot([0.25, 0.25], [1.0, 3.0], color='black', lw=1.5)
    # ground
    for x in np.linspace(0.25, 4.7, 18):
        ax.plot([x, x - 0.25], [1.0, 0.75], color='gray', lw=0.8)
    ax.plot([0.25, 4.8], [1.0, 1.0], color='black', lw=1.5)

    # spring (zigzag) — upper lane
    x_start, x_end, y_spring, n_coils = 0.25, 1.7, 2.15, 5
    xs = np.linspace(x_start, x_end, n_coils * 2 + 2)
    ys = np.zeros_like(xs)
    ys[0], ys[-1] = y_spring, y_spring
    for i in range(1, len(xs) - 1):
        ys[i] = y_spring + (0.18 if i % 2 == 1 else -0.18)
    ax.plot(xs, ys, color='#008b9a', lw=2.0)
    ax.text((x_start + x_end) / 2 - 0.4, y_spring + 0.22, r'$c$', ha='center',
            va='bottom', fontsize=14, color='#008b9a')

    # damper — lower lane: outer box + inner rod
    y_damp, d_x0, d_x1, box_w, box_h = 1.45, 0.25, 1.7, 0.4, 0.4
    d_mid = (d_x0 + d_x1) / 2
    # left rod
    ax.plot([d_x0, d_mid - box_w / 2], [y_damp, y_damp], color='#006371',
            lw=2.0)
    # box (dashpot body)
    ax.plot([d_mid - box_w / 2, d_mid - box_w / 2],
            [y_damp - box_h / 2 - 0.05, y_damp + box_h / 2 + 0.05],
            color='#006371', lw=2.5)
    ax.plot([d_mid - box_w / 2, d_mid + 0.1],
            [y_damp - box_h / 2 - 0.05, y_damp - box_h / 2 - 0.05],
            color='#006371', lw=2.5)
    ax.plot([d_mid - box_w / 2, d_mid + 0.1],
            [y_damp + box_h / 2 + 0.05, y_damp + box_h / 2 + 0.05],
            color='#006371', lw=2.5)
    # inner piston rod (shorter, centered)
    ax.plot([d_mid, d_x1], [y_damp, y_damp], color='#006371', lw=2.0)
    # piston cap inside box
    ax.plot([d_mid, d_mid],
            [y_damp - box_h / 2 + 0.08, y_damp + box_h / 2 - 0.08],
            color='#006371', lw=3.0)
    ax.text(d_mid - 0.4, y_damp + box_h / 2 + 0.13, r'$d$', ha='center',
            va='top', fontsize=14, color='#006371')

    # mass block
    mass_x, mass_y, mass_w, mass_h = 1.75, 1.3, 1.5, 1.0
    rect = mpatches.FancyBboxPatch((mass_x, mass_y), mass_w, mass_h,
                                   boxstyle='round,pad=0.05', linewidth=1.5,
                                   edgecolor='black', facecolor='#a8dadc')
    ax.add_patch(rect)
    ax.text(mass_x + mass_w / 2, mass_y + mass_h / 2, r'$m$', ha='center',
            va='center', fontsize=14)

    # force arrow
    ax.annotate('', xy=(mass_x + mass_w + 0.8, mass_y + mass_h / 2),
                xytext=(mass_x + mass_w, mass_y + mass_h / 2),
                arrowprops=dict(arrowstyle='->', color='#e63946', lw=2.0))
    ax.text(mass_x + mass_w + 0.9, mass_y + mass_h / 2, r'$f_{\mathrm{ex}}$',
            ha='left', va='center', fontsize=14, color='#e63946')

    # displacement arrow
    arrow_y = mass_y + 1.5
    ax.annotate('', xy=(mass_x + mass_w * 0.8, arrow_y),
                xytext=(mass_x + mass_w * 0.2, arrow_y),
                arrowprops=dict(arrowstyle='->', color='dimgray', lw=1.5))
    ax.text(mass_x + mass_w / 2, arrow_y - 0.12, r'$q$', ha='center',
            va='top', fontsize=14, color='dimgray')

    # rollers
    for rx in [mass_x + 0.4, mass_x + 1.1]:
        ax.add_patch(plt.Circle((rx, 1.13), 0.11, color='gray', zorder=3))

    plt.show()


def draw_nonlinear_Duffing_system():
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    ax.axis('off')

    # --- wall ---
    for y in np.linspace(0.5, 3.5, 10):
        ax.plot([0.0, 0.25], [y, y + 0.25], color='gray', lw=1.0)
    ax.plot([0.25, 0.25], [0.5, 3.75], color='black', lw=1.5)

    # --- ground ---
    ax.plot([0.25, 5.8], [0.5, 0.5], color='black', lw=1.5)
    for x in np.linspace(0.25, 5.7, 20):
        ax.plot([x, x - 0.2], [0.5, 0.28], color='gray', lw=0.8)

    # --- linear spring (top lane) ---
    x0, x1, y_sp = 0.25, 1.9, 2.6
    n = 5
    xs = np.linspace(x0, x1, n * 2 + 2)
    ys = np.zeros_like(xs)
    ys[0] = ys[-1] = y_sp
    for i in range(1, len(xs)-1):
        ys[i] = y_sp + (0.18 if i % 2 == 1 else -0.18)
    ax.plot(xs, ys, color='#008b9a', lw=2.0)
    ax.text((x0+x1)/2 - 0.4, y_sp + 0.25, r'$c$', ha='center', va='bottom',
            fontsize=14, color='#008b9a')

    # damper — lower lane: outer box + inner rod
    y_damp, d_x0, d_x1, box_w, box_h = 1.9, 0.25, 1.9, 0.4, 0.4
    d_mid = (d_x0 + d_x1) / 2
    # left rod
    ax.plot([d_x0, d_mid - box_w / 2], [y_damp, y_damp], color='#006371',
            lw=2.0)
    # box (dashpot body)
    ax.plot([d_mid - box_w / 2, d_mid - box_w / 2],
            [y_damp - box_h / 2 - 0.05, y_damp + box_h / 2 + 0.05],
            color='#006371', lw=2.5)
    ax.plot([d_mid - box_w / 2, d_mid + 0.1],
            [y_damp - box_h / 2 - 0.05, y_damp - box_h / 2 - 0.05],
            color='#006371', lw=2.5)
    ax.plot([d_mid - box_w / 2, d_mid + 0.1],
            [y_damp + box_h / 2 + 0.05, y_damp + box_h / 2 + 0.05],
            color='#006371', lw=2.5)
    # inner piston rod (shorter, centered)
    ax.plot([d_mid, d_x1], [y_damp, y_damp], color='#006371', lw=2.0)
    # piston cap inside box
    ax.plot([d_mid, d_mid],
            [y_damp - box_h / 2 + 0.08, y_damp + box_h / 2 - 0.08],
            color='#006371', lw=3.0)
    ax.text(d_mid - 0.4, y_damp + box_h / 2 + 0.13, r'$d$', ha='center',
            va='top', fontsize=14, color='#006371')

    # --- nonlinear spring ---
    x0, x1, y_sp = 0.25, 1.9, 1.2
    n = 5
    xs = np.linspace(x0, x1, n * 2 + 2)
    ys = np.zeros_like(xs)
    ys[0] = ys[-1] = y_sp
    for i in range(1, len(xs)-1):
        ys[i] = y_sp + (0.18 if i % 2 == 1 else -0.18)
    ax.plot(xs, ys, color='#f19699', lw=2.0)
    ax.text((x0+x1)/2 - 0.4, y_sp + 0.25, r'$\alpha$', ha='center',
            va='bottom', fontsize=14, color='#f19699')
    ax.annotate('', xy=(x1 - 0.4, y_sp + 0.4), xytext=(x0 + 0.4, y_sp - 0.4),
                arrowprops=dict(arrowstyle='->', color='#f19699', lw=2.0))

    # --- mass block ---
    mass_x, mass_y, mass_w, mass_h = 1.95, .85, 1.75, 2.
    ax.add_patch(mpatches.FancyBboxPatch((mass_x, mass_y), mass_w, mass_h,
                                         boxstyle='round,pad=0.05',
                                         linewidth=1.5, edgecolor='black',
                                         facecolor='#a8dadc'))
    ax.text(mass_x + mass_w/2, mass_y + mass_h/2, r'$m$', ha='center',
            va='center', fontsize=14)

    # --- rollers ---
    for rx in [mass_x + 0.4, mass_x + 1.4]:
        ax.add_patch(plt.Circle((rx, 0.65), 0.15, color='gray', zorder=3))

    # --- force arrow ---
    ax.annotate('', xy=(mass_x + mass_w + 0.85, mass_y + mass_h/2),
                xytext=(mass_x + mass_w, mass_y + mass_h/2),
                arrowprops=dict(arrowstyle='->', color='#e63946', lw=2.0))
    ax.text(mass_x + mass_w + 0.95, mass_y + mass_h/2, r'$f_{\mathrm{ex}}$',
            ha='left', va='center', fontsize=14, color='#e63946')

    # --- displacement arrow ---
    arrow_y = mass_y + mass_h + 0.35
    ax.annotate('', xy=(mass_x + mass_w*0.8, arrow_y),
                xytext=(mass_x + mass_w*0.2, arrow_y),
                arrowprops=dict(arrowstyle='->', color='dimgray', lw=1.5))
    ax.text(mass_x + mass_w/2, arrow_y + 0.08, r'$q$', ha='center',
            va='bottom', fontsize=14, color='dimgray')

    # --- small force-displacement inset (hardening curve) ---
    inset = fig.add_axes([0.72, 0.55, 0.22, 0.32])
    q_ins = np.linspace(-1, 1, 200)
    inset.plot(q_ins, q_ins + 0.6*q_ins**3, color='#f19699', lw=1.8)
    inset.plot(q_ins, q_ins,                color='#008b9a', lw=1.2, ls='--')
    inset.axhline(0, color='black', lw=0.5)
    inset.axvline(0, color='black', lw=0.5)
    inset.set_xticks([])
    inset.set_yticks([])
    inset.set_xlabel(r'$q$', fontsize=9, labelpad=2)
    inset.set_ylabel(r'$f$', fontsize=9, labelpad=5, rotation=0)
    inset.set_title('hardening', fontsize=8, pad=3)

    plt.show()


def draw_nonlinear_Jenkins_system():
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    ax.axis('off')

    # --- wall ---
    for y in np.linspace(0.5, 3.5, 10):
        ax.plot([0.0, 0.25], [y, y + 0.25], color='gray', lw=1.0)
    ax.plot([0.25, 0.25], [0.5, 3.75], color='black', lw=1.5)

    # --- ground ---
    ax.plot([0.25, 5.8], [0.5, 0.5], color='black', lw=1.5)
    for x in np.linspace(0.25, 5.7, 20):
        ax.plot([x, x - 0.2], [0.5, 0.28], color='gray', lw=0.8)

    # --- linear spring (top lane) ---
    x0, x1, y_sp = 0.25, 1.9, 2.6
    n = 5
    xs = np.linspace(x0, x1, n * 2 + 2)
    ys = np.zeros_like(xs)
    ys[0] = ys[-1] = y_sp
    for i in range(1, len(xs)-1):
        ys[i] = y_sp + (0.18 if i % 2 == 1 else -0.18)
    ax.plot(xs, ys, color='#008b9a', lw=2.0)
    ax.text((x0+x1)/2 - 0.4, y_sp + 0.25, r'$c$', ha='center', va='bottom',
            fontsize=12, color='#008b9a')

    # --- damper (middle lane) ---
    y_damp, d_x0, d_x1, box_w, box_h = 1.9, 0.25, 1.9, 0.4, 0.4
    d_mid = (d_x0 + d_x1) / 2
    ax.plot([d_x0, d_mid - box_w / 2], [y_damp, y_damp], color='#006371',
            lw=2.0)
    ax.plot([d_mid - box_w / 2, d_mid - box_w / 2],
            [y_damp - box_h/2 - 0.05, y_damp + box_h/2 + 0.05],
            color='#006371', lw=2.5)
    ax.plot([d_mid - box_w / 2, d_mid + 0.1],
            [y_damp - box_h/2 - 0.05, y_damp - box_h/2 - 0.05],
            color='#006371', lw=2.5)
    ax.plot([d_mid - box_w / 2, d_mid + 0.1],
            [y_damp + box_h/2 + 0.05, y_damp + box_h/2 + 0.05],
            color='#006371', lw=2.5)
    ax.plot([d_mid, d_x1], [y_damp, y_damp], color='#006371', lw=2.0)
    ax.plot([d_mid, d_mid],
            [y_damp - box_h/2 + 0.08, y_damp + box_h/2 - 0.08],
            color='#006371', lw=3.0)
    ax.text(d_mid - 0.4, y_damp + box_h/2 + 0.13, r'$d$', ha='center',
            va='top', fontsize=12, color='#006371')

    # --- Jenkins element (bottom lane): spring k with friction slider ---
    y_jk, jk_x0, jk_x1 = 1.2, 0.9, 1.9

    # left rod to Jenkins spring
    x_sp0, x_sp1 = jk_x0, jk_x1
    n_j = 3
    xs_j = np.linspace(x_sp0, x_sp1, n_j * 2 + 2)
    ys_j = np.zeros_like(xs_j)
    ys_j[0] = ys_j[-1] = y_jk
    for i in range(1, len(xs_j)-1):
        ys_j[i] = y_jk + (0.18 if i % 2 == 1 else -0.18)
    ax.plot(xs_j, ys_j, color='#f19699', lw=2.0)
    ax.text((x_sp0 + x_sp1)/2 + 0.15, y_jk + 0.2, r'$k$', ha='center',
            va='bottom', fontsize=12, color='#f19699')

    # right rod from slider to mass
    ax.plot([jk_x0, jk_x0], [0.5, y_jk], color='#f19699', lw=2.0)
    ax.annotate('', xy=(jk_x0, 0.5), xytext=(jk_x0, y_jk),
                arrowprops=dict(arrowstyle='->', color='#f19699', lw=2.0))
    ax.text(jk_x0 - 0.5, (0.5 + y_jk)/2, r'$\mu N$', ha='left', va='center',
            fontsize=12, color='#f19699')

    # --- mass block ---
    mass_x, mass_y, mass_w, mass_h = 1.95, 0.85, 1.75, 2.0
    ax.add_patch(mpatches.FancyBboxPatch((mass_x, mass_y), mass_w, mass_h,
                                         boxstyle='round,pad=0.05',
                                         linewidth=1.5, edgecolor='black',
                                         facecolor='#a8dadc'))
    ax.text(mass_x + mass_w/2, mass_y + mass_h/2, r'$m$', ha='center',
            va='center', fontsize=14)

    # --- rollers ---
    for rx in [mass_x + 0.4, mass_x + 1.4]:
        ax.add_patch(plt.Circle((rx, 0.65), 0.15, color='gray', zorder=3))

    # --- force arrow ---
    ax.annotate('', xy=(mass_x + mass_w + 0.85, mass_y + mass_h/2),
                xytext=(mass_x + mass_w, mass_y + mass_h/2),
                arrowprops=dict(arrowstyle='->', color='#e63946', lw=2.0))
    ax.text(mass_x + mass_w + 0.95, mass_y + mass_h/2, r'$f_{\mathrm{ex}}$',
            ha='left', va='center', fontsize=14, color='#e63946')

    # --- displacement arrow ---
    arrow_y = mass_y + mass_h + 0.35
    ax.annotate('', xy=(mass_x + mass_w*0.8, arrow_y),
                xytext=(mass_x + mass_w*0.2, arrow_y),
                arrowprops=dict(arrowstyle='->', color='dimgray', lw=1.5))
    ax.text(mass_x + mass_w/2, arrow_y + 0.08, r'$q$', ha='center',
            va='bottom', fontsize=14, color='dimgray')

    # --- inset: hysteresis loop ---
    inset = fig.add_axes([0.72, 0.55, 0.22, 0.32])
    # piecewise hysteresis loop: stick phases and slip phases
    t = np.linspace(0, 2*np.pi, 500)
    q_ins = np.sin(t)
    # approximate Jenkins hysteresis loop parametrically
    f_ins = np.zeros_like(q_ins)
    k = 1.5
    fs = 0.5
    state = 0.0
    for i in range(1, len(q_ins)):
        trial = state + k * (q_ins[i] - q_ins[i-1])
        f_ins[i] = np.clip(trial, -fs, fs)
        state = f_ins[i]
    inset.plot(q_ins, f_ins, color='#f19699', lw=1.8)
    inset.axhline(0, color='black', lw=0.5)
    inset.axvline(0, color='black', lw=0.5)
    inset.set_xticks([])
    inset.set_yticks([])
    inset.set_xlabel(r'$q$', fontsize=9, labelpad=2)
    inset.set_ylabel(r'$f$', fontsize=9, labelpad=5, rotation=0)
    inset.set_title('stick-slip', fontsize=8, pad=3)

    plt.show()
