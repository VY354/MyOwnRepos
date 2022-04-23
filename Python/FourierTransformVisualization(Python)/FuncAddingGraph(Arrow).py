import pyautogui
from math import *
import numpy as np
import matplotlib
import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation, writers

# ===============================================================================
# ===============================================================================


def getFuncList(angles, amplitudeList, freqList, phaseList):
    funcList = []
    for i in range(min(len(amplitudeList), len(freqList))):
        f = amplitudeList[i] * np.sin(freqList[i] * angles + phaseList[i])+1
        funcList.append(f)
    return funcList

def wrap(angles, freqList, wf):
    if type(angles) is float:
        angles = np.array([angles])
    funcs = getFuncList(angles, amplitudeList, freqList, phaseList)
    func = np.zeros(len(angles))
    for i in funcs:
        func += i

    x = np.cos(wf * angles)
    y = np.sin(wf * angles)

    fx = func * x
    fy = func * y

    if len(angles) == 1:
        return fx[0], fy[0]
    return fx, fy

# ===============================================================================

fig = plt.figure(figsize=(12, 7))

axes_mainGrapth = fig.add_subplot(211)
axes_mainGrapthCircle = fig.add_subplot(212)
axes_mainGrapth.axis('off')
axes_mainGrapthCircle.axis('off')
axes_mainGrapthCircle.axis('equal')
# ===============================================================================

minA = 0
maxA = 2 * pi
dA = 0.01

ff = 1
wf = 1

plotsNum = 3

angles = np.arange(minA, maxA, dA)

amplitudeList = np.array([1,1,1])
freqList = np.array([2,5,9])*1
phaseList = np.array([0,0,0])

# amplitudeList = [i for i in range(1, plotsNum + 1)]
# freqList = [i for i in range(1, plotsNum + 1)]
# phaseList = [0 for i in range(1, plotsNum + 1)]

# print(amplitudeList)
# print(freqList)
# print(phaseList)

plots = getFuncList(angles, amplitudeList, freqList, phaseList)

mainPlot = np.zeros(len(angles))
for i in plots:
    mainPlot += i

# ===============================================================================

offset1 = 0.5
mnx = angles.min() - offset1
mxx = angles.max() + offset1
mny = mainPlot.min() - offset1
mxy = mainPlot.max() + offset1

axes_mainGrapth.set_xlim(mnx, mxx)
axes_mainGrapth.set_ylim(mny, mxy)

# ===============================================================================

line_mainPlot, = axes_mainGrapth.plot(angles, mainPlot, lw=1.5, ls='-', c='blue', zorder=0)
axes_mainGrapth.hlines(y=mainPlot.min(), xmin=0, xmax=angles.max(), colors=['darkgrey'])

line_arrow_main, = axes_mainGrapth.plot([], [], lw=2, ls='-', c='red', zorder=1)
scatter_arrowPoint = axes_mainGrapth.scatter([], [], s=15 * pi, color='red', zorder=2)

axes_mainGrapthCircle.hlines(y=0, xmin=-mxy, xmax=mxy, colors=['darkgrey'], lw=1)
axes_mainGrapthCircle.vlines(x=0, ymin=-mxy, ymax=mxy, colors=['darkgrey'], lw=1)

wrapX, wrapY = wrap(angles, freqList, wf)
line_wrapGraph, = axes_mainGrapthCircle.plot(wrapX, wrapY, lw=1.5, ls='-', c='blue', zorder=1)

line_arrow_circle, = axes_mainGrapthCircle.plot([], [], lw=2, ls='-', c='red', zorder=2)
scatter_arrowPoint_circle = axes_mainGrapthCircle.scatter([], [], s=15 * pi, color='red', zorder=3)

# ===============================================================================

w = 0.005
def anim(t):
    dt = abs(((w * t) % 1) * maxA)

    funcs = getFuncList(np.array([dt]), amplitudeList, freqList, phaseList)

    y = np.zeros((1))
    for i in funcs:
        y += i

    arrowX_main = [dt, dt]
    arrowY_main = [mainPlot.min(), y]

    line_arrow_main.set_data(arrowX_main, arrowY_main)
    scatter_arrowPoint.set_offsets([dt, y])

    arrowX_circle, arrowY_circle = wrap(dt, freqList, wf)
    line_arrow_circle.set_data([0, arrowX_circle], [0, arrowY_circle])
    scatter_arrowPoint_circle.set_offsets([arrowX_circle, arrowY_circle])

    return scatter_arrowPoint, line_arrow_main, line_arrow_circle, scatter_arrowPoint_circle,

# ===============================================================================

animation1 = FuncAnimation(fig=fig, func=anim, interval=1, blit=True,frames=int(2*pi/w))

# ===============================================================================
# ===============================================================================

path = r"F:\From Disk Windows 7 SSD\Home Work\Different\Essence of Fourier Transform\Gifs\FAddArrowAnim(1).gif"
matplotlib.rcParams['animation.ffmpeg_path'] = r"C:\ffmpeg (доп. ПО длясохранения видео) - ярлык\ffmpeg-4.4-full_build\bin\ffmpeg.exe"
writervideo = matplotlib.animation.FFMpegWriter(fps=30)
#animation1.save(path,writervideo)

# ===============================================================================

plt.interactive(False)
plt.tight_layout()

# PlotManager = plt.get_current_fig_manager()
# PlotManager.window.state('zoomed')

plt.show()
plt.close()
