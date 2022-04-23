import pyautogui
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation, writers

# ===============================================================================
# ===============================================================================

def f(angles):
    return np.sin(angles)


def wrap(angles, ff, wf):
    func = f(ff * angles) + 1

    x = np.cos(wf * angles)
    y = np.sin(wf * angles)

    fx = func * x
    fy = func * y

    return fx, fy

# ===============================================================================

fig = plt.figure(figsize=(12, 7))

axes_mainGrapth = fig.add_subplot(221)
axes_COM_xc_yc = fig.add_subplot(222)
axes_COM_t_yc = fig.add_subplot(212)

axes_mainGrapth.axis('equal')
axes_COM_xc_yc.axis('equal')
axes_COM_t_yc.axis('equal')

# ===============================================================================

startA = 0
endA = 10 * pi
dA = 0.001

angles = np.arange(startA, endA, dA)
fa = wrap(angles, 1, 1)

# ===============================================================================

offset1=4
mnx = -fa[0].max() - offset1
mxx = fa[0].max() + offset1
mny = -fa[1].max() - offset1
mxy = fa[1].max() + offset1

axes_mainGrapth.set_xlim(mnx, mxx)
axes_mainGrapth.set_ylim(mny, mxy)

offset2=5
axes_COM_xc_yc.set_xlim(mnx+offset2, mxx-offset2)
axes_COM_xc_yc.set_ylim(mny+offset2, mxy-offset2)

axes_COM_t_yc.set_ylim(-0.2, 0.7)

# ===============================================================================

line_mainPlot, = axes_mainGrapth.plot(fa[0], fa[1], lw=2, ls='-', c='blue', zorder=0)

x_COM_line = []
y_COM_line = []
line_COM_t_yc, = axes_COM_t_yc.plot(angles, angles, lw=2, ls='-', c='red', zorder=0)

x_COM_line2 = []
line_COM_xc_yc, = axes_COM_xc_yc.plot(angles, angles, lw=1, ls='-', c='red', zorder=0)

scatter_COM = axes_mainGrapth.scatter([], [], s=10 * pi, c='red', zorder=1)

# ===============================================================================

axes_COM_t_yc.set_xlim(0, 10)
axes_COM_t_yc.set_xticks(np.arange(0, 10, 0.5))
axes_COM_t_yc.set_ylim(-0.2, 0.7)

w=0.01
def anim(t):
    dt = w * (t)

    x, y = wrap(angles, 3, dt)

    x_COM = x.mean()
    y_COM = y.mean()

    x_COM_line.append(dt)
    x_COM_line2.append(x_COM)
    y_COM_line.append(y_COM)

    line_mainPlot.set_data(x, y)
    line_COM_t_yc.set_data(x_COM_line, y_COM_line)
    line_COM_xc_yc.set_data(x_COM_line2, y_COM_line)
    scatter_COM.set_offsets([[x_COM, y_COM]])

    return line_mainPlot, line_COM_t_yc, line_COM_xc_yc, scatter_COM,


animation1 = FuncAnimation(fig=fig, func=anim, interval=1, blit=True,frames=1000)

# ===============================================================================
# ===============================================================================

path= r"F:\From Disk Windows 7 SSD\PyCharm Projects\COMv2Anim.gif"
matplotlib.rcParams['animation.ffmpeg_path'] = r"C:\ffmpeg (доп. ПО длясохранения видео) - ярлык\ffmpeg-4.4-full_build\bin\ffmpeg.exe"
writervideo = matplotlib.animation.FFMpegWriter(fps=24)
# animation1.save(path,writervideo)

# ===============================================================================

plt.interactive(False)

plt.grid(b=True,axis='both')
plt.tight_layout()

# PlotManager = plt.get_current_fig_manager()
# PlotManager.window.state('zoomed')

plt.show()

