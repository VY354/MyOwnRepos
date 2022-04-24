import pyautogui
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation, writers
import keyboard

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

axes_mainGrapth = fig.add_subplot(211)
axes_COM_t_yc = fig.add_subplot(212)

axes_mainGrapth.axis('equal')
axes_COM_t_yc.axis('equal')

# ===============================================================================

startA = 0
endA = 2 * pi
dA = 0.001

angles = np.arange(startA, endA, dA)
fa = wrap(angles, 1, 1)

# ===============================================================================

offset1=1
mnx = -fa[0].max() - offset1
mxx = fa[0].max() + offset1
mny = -fa[1].max() - offset1
mxy = fa[1].max() + offset1

axes_mainGrapth.set_xlim(mnx, mxx)
axes_mainGrapth.set_ylim(mny, mxy)

axes_COM_t_yc.set_ylim(-0.2, 0.7)

# ===============================================================================

line_mainPlot, = axes_mainGrapth.plot(fa[0], fa[1], lw=2, ls='-', c='blue', zorder=0)

x_COM_line = []
y_COM_line = []
line_COM_t_yc, = axes_COM_t_yc.plot(angles, angles, lw=2, ls='-', c='red', zorder=0)

scatter_COM = axes_mainGrapth.scatter([], [], s=10 * pi, c='red', zorder=1)

# ===============================================================================

axes_COM_t_yc.set_xlim(0, 10)
axes_COM_t_yc.set_xticks(np.arange(0, 10, 0.5))
axes_COM_t_yc.set_ylim(-0.2, 0.7)

w=10
def anim(t):

    if keyboard.is_pressed('c'):
        x_COM_line.clear()
        y_COM_line.clear()

    dtx = pyautogui.position().x / pyautogui.size()[0] * w
    dty = (1 - pyautogui.position().y / pyautogui.size()[1]) * w

    x, y = wrap(angles, dtx, dty)

    xc = x.mean()
    yc = y.mean()

    x_COM_line.append(dtx)
    y_COM_line.append(yc)

    line_mainPlot.set_data(x, y)
    line_COM_t_yc.set_data(x_COM_line, y_COM_line)
    scatter_COM.set_offsets([[xc, yc]])

    return line_mainPlot, line_COM_t_yc, scatter_COM,


animation1 = FuncAnimation(fig=fig, func=anim, interval=0, blit=True)

# ===============================================================================
# ===============================================================================

plt.interactive(False)

plt.grid(b=True, axis='both')
plt.tight_layout()

PlotManager = plt.get_current_fig_manager()
PlotManager.window.state('zoomed')

plt.show()
