import pyautogui
from math import *
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation, writers

# ===============================================================================
# ===============================================================================

def f(angles):
    return np.sin(angles)+np.sin(2*angles)


def wrap(angles,ff, wf):

    func = f(ff*angles)+1

    x = np.cos(wf * angles)
    y = np.sin(wf * angles)

    fx = func * x
    fy = func * y

    return fx, fy

# ===============================================================================

fig = plt.figure(figsize=(12, 7))

axes_mainGrapth = fig.add_subplot(111)
axes_mainGrapth.axis('equal')
axes_mainGrapth.axis('off')
#axes_mainGrapth.figure.set_size_inches(9,5)

# ===============================================================================

startA = 0
endA = 2 * pi
dA = 0.001

angles = np.arange(startA, endA, dA)
fa = wrap(angles,1,1)

# ===============================================================================

offset1=4
mnx = -fa[0].max() - offset1
mxx = fa[0].max() + offset1
mny = -fa[1].max() - offset1
mxy = fa[1].max() + offset1

axes_mainGrapth.set_xlim(mnx,mxx)
axes_mainGrapth.set_ylim(mny,mxy)

# ===============================================================================
text_funcFreq=axes_mainGrapth.text(mnx,2,'a',fontsize=20)
text_wrapFreq=axes_mainGrapth.text(mnx,1.5,'b',fontsize=20)

line, = axes_mainGrapth.plot(fa[0], fa[1], lw=2, ls='-', c='blue',zorder=0)

w=5
def anim(t):

    dtx = pyautogui.position().x/pyautogui.size()[0]*w
    dty = (1-pyautogui.position().y/pyautogui.size()[1])*w
    x, y = wrap(angles, dtx, dty)
    line.set_data(x, y)

    text_funcFreq.set_text('частота сигнала = ' + str(round(dtx,3)))
    text_wrapFreq.set_text('частота оборачивания = ' + str(round(dty,3)))

    return line, text_funcFreq,text_wrapFreq,

animation1 = FuncAnimation(fig=fig, func=anim, interval=0, blit=True)

# ===============================================================================
# ===============================================================================

plt.interactive(False)

plt.grid(b=False,axis='both')
plt.tight_layout()

PlotManager = plt.get_current_fig_manager()
PlotManager.window.state('zoomed')

plt.show()