from math import *
import random
import numpy as np
import matplotlib
import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation, writers
import pyautogui
from perlin_noise import perlin_noise

# ===============================================================================
# ===============================================================================

def getFuncList(angles, amplitudeList, freqList, phaseList):
    funcList = []
    funcList.append([0])
    for i in range(1, min(len(amplitudeList), len(freqList))):
        f = amplitudeList[i] * np.sin(freqList[i] * angles + phaseList[i])
        funcList.append(f)
    f = np.zeros((len(angles)))
    for i in range(1, len(funcList)):
        f += funcList[i]
    funcList[0] = f
    return funcList

# ===============================================================================

plotsNum = 3 + 1

fig = plt.figure(figsize=(12, 7))

axesList = []
for i in range(plotsNum):
    ax = fig.add_subplot(plotsNum, 1, i + 1)
    axesList.append(ax)

# ===============================================================================

minA = 0
maxA = 2 * pi
dA = 0.01
angles = np.arange(minA, maxA, dA)

amplitudeList = np.linspace(1, pi, plotsNum)
freqList = np.linspace(1, 3, plotsNum) * 10
phaseList = np.linspace(0, pi, plotsNum)
plots = getFuncList(angles, amplitudeList, freqList, phaseList)

# ===============================================================================

offset1 = 1
mnx = angles.min() - offset1 / 2
mxx = angles.max() + offset1 / 2
mny = plots[0].min() - offset1
mxy = plots[0].max() + offset1

# ===============================================================================


for ax in axesList:
    ax.set_xlim(mnx, mxx)
    ax.set_ylim(mny, mxy)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

lines = []
for ax in axesList:
    l = ax.plot([], [], lw=1.5, ls='-', c='blue')
    lines.append(l)
lines[0][0].set_linewidth(3)

# ===============================================================================

dCLR = 255 / (len(plots))
CLR = dCLR

w = 0.001
noise = perlin_noise.PerlinNoise()


def anim(t):
    dt = w * t

    amplitudeList = np.array([noise(i * dt+10*1.618)*10 for i in np.linspace(1, 4, plotsNum)])
    freqList = np.array([noise(i * dt+100*pi)*100 for i in np.linspace(1, 4, plotsNum)])
    phaseList = np.array([noise(i * dt+1000*e)*50 for i in np.linspace(1, 4, plotsNum)])
    plots = getFuncList(angles, amplitudeList, freqList, phaseList)

    offset1 = 1
    mnx = angles.min() - offset1 / 2
    mxx = angles.max() + offset1 / 2
    mny = -plots[0].max() - offset1
    mxy = plots[0].max() + offset1

    for ax in axesList:
        ax.set_xlim(mnx, mxx)
        ax.set_ylim(mny, mxy)

    dCLR = 255 / (len(plots))
    CLR = dCLR
    for (l, p) in zip(lines, plots):
        l[0].set_data(angles, p)
        l[0].set_color(matplotlib.colors.to_rgb((0, 1 - CLR / 255, 0)))
        CLR += dCLR

    return (l[0] for l in lines)

# ===============================================================================

animation1 = FuncAnimation(fig=fig, func=anim, interval=1, blit=True,frames=int(2*pi/w*0.1))

# ===============================================================================
# ===============================================================================

path= r"F:\From Disk Windows 7 SSD\Home Work\Different\Essence of Fourier Transform\Gifs\FAddAnim.gif"
matplotlib.rcParams['animation.ffmpeg_path'] = r"C:\ffmpeg (доп. ПО длясохранения видео) - ярлык\ffmpeg-4.4-full_build\bin\ffmpeg.exe"
writervideo = matplotlib.animation.FFMpegWriter(fps=30)
#animation1.save(path,writervideo)

# ===============================================================================

plt.interactive(False)
plt.tight_layout()

# PlotManager = plt.get_current_fig_manager()
# PlotManager.window.state('zoomed')

plt.show()
