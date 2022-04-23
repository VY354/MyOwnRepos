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

def getFuncList(angles, amplitudeList, freqList, phaseList):
    funcList = []
    for i in range(len(amplitudeList)):
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
axes_COM_t_yc = fig.add_subplot(212)

axes_mainGrapth.axis('equal')

# ===============================================================================

minA = 0
maxA = 2 * pi
dA = 0.01

ff = 3
wf = 1

plotsNum = 3

angles = np.arange(minA, maxA, dA)

amplitudeList = np.array([1,1,1])*7
freqList = np.array([2,5,9])*1
phaseList = np.array([0,0,0])

# amplitudeList = [2 for i in range(1, plotsNum + 1)]
# freqList = [2,5,7]
# phaseList = [0 for i in range(1, plotsNum + 1)]

plots = wrap(angles,freqList, 1)

mainPlot = np.zeros(len(angles))
for i in plots:
    mainPlot += i

# ===============================================================================

offset1=0
mnx = -mainPlot.max() - offset1
mxx = mainPlot.max() + offset1
mny = -mainPlot.max() - offset1
mxy = mainPlot.max() + offset1

axes_mainGrapth.set_xlim(mnx, mxx)
axes_mainGrapth.set_ylim(mny, mxy)

axes_COM_t_yc.set_ylim(-1, 4.5)

# ===============================================================================

line_mainPlot, = axes_mainGrapth.plot(angles, mainPlot, lw=1.5, ls='-', c='blue', zorder=0)

x_COM_line = []
y_COM_line = []
line_COM_t_yc, = axes_COM_t_yc.plot(angles, angles, lw=2, ls='-', c='red', zorder=0)
scatter_COM = axes_mainGrapth.scatter([], [], s=10 * pi, c='red', zorder=1)

# ===============================================================================

axes_COM_t_yc.set_xlim(0, 11)
axes_COM_t_yc.set_xticks(np.arange(0, 12, 0.5))

w=0.0025
def anim(t):
    dt = abs(((w * t)%1 * 12))

    x, y = wrap(angles, freqList, dt)

    x_COM = x.mean()
    y_COM = y.mean()

    x_COM_line.append(dt)
    y_COM_line.append(y_COM)

    if abs((w*t)%1-1) < 0.01:
        x_COM_line.clear()
        y_COM_line.clear()

    line_mainPlot.set_data(x, y)
    line_COM_t_yc.set_data(x_COM_line, y_COM_line)
    scatter_COM.set_offsets([[x_COM, y_COM]])

    return line_mainPlot, line_COM_t_yc, scatter_COM,

animation1 = FuncAnimation(fig=fig, func=anim, interval=1, blit=True,frames=int(1/w))

# ===============================================================================
# ===============================================================================

path= r"F:\From Disk Windows 7 SSD\Home Work\Different\Essence of Fourier Transform\Gifs\COMv1Anim.gif"
matplotlib.rcParams['animation.ffmpeg_path'] = r"C:\ffmpeg (доп. ПО длясохранения видео) - ярлык\ffmpeg-4.4-full_build\bin\ffmpeg.exe"
writervideo = matplotlib.animation.FFMpegWriter(fps=30)
animation1.save(path,writervideo)

# ===============================================================================

plt.interactive(False)

plt.grid(b=True, axis='both')
plt.tight_layout()

# PlotManager = plt.get_current_fig_manager()
# PlotManager.window.state('zoomed')

plt.show()
