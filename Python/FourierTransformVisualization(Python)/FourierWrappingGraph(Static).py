import pyautogui
from math import *
import numpy as np
import matplotlib as mpl
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

axes_mainGrapth = fig.add_subplot(111)
axes_mainGrapth.axis('equal')
axes_mainGrapth.axis('off')
axes_mainGrapth.figure.set_size_inches(12,7)

# ===============================================================================

minA = 0
maxA = 2 * pi
dA = 0.01

ff = 1
wf = 1

plotsNum = 1

angles = np.arange(minA, maxA, dA)

amplitudeList = np.array([1,1,1])
freqList = np.array([2,5,9])*1
phaseList = np.array([0,0,0])

# amplitudeList = np.array([i for i in range(1, plotsNum + 1)])
# freqList = np.array([3 for i in range(1, plotsNum + 1)])
# phaseList = np.array([0 for i in range(1, plotsNum + 1)])

plots = getFuncList(angles, amplitudeList, freqList, phaseList)

mainPlot = np.zeros(len(angles))
for i in plots:
    mainPlot += i

x, y = wrap(angles, freqList, wf)

# ===============================================================================

offset1 = 2
mnx = mainPlot.min() - 0
mxx = mainPlot.max() + 0
mny = -mainPlot.max() - 0.5
mxy = mainPlot.max() + 0.5

axes_mainGrapth.set_xlim(mnx, mxx)
axes_mainGrapth.set_ylim(mny, mxy)

text_funcFreq=axes_mainGrapth.text(0.01,0.9,'a',fontsize=16,horizontalalignment='left', verticalalignment='center',transform = axes_mainGrapth.transAxes)
text_wrapFreq=axes_mainGrapth.text(0.01,0.8,'b',fontsize=16,horizontalalignment='left', verticalalignment='center',transform = axes_mainGrapth.transAxes)

# ===============================================================================

text_funcFreq.set_text('частоты сигнала = {0}'.format('; '.join(map(str,freqList))))
text_wrapFreq.set_text('частота оборачивания = ' + str(round(wf, 3)))

line_mainPlot, = axes_mainGrapth.plot(x+mxx, y, lw=2, ls='-', c='blue',zorder=0)
scatter_COM = axes_mainGrapth.scatter([], [], s=30 * pi, c='red', zorder=1)

x_COM = x.mean()
y_COM = y.mean()
scatter_COM.set_offsets([[x_COM+mxx, y_COM]])

# ===============================================================================
# ===============================================================================

#plt.savefig(fname = r"F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\FourierExample\results\test.png", dpi=100)

# ===============================================================================

plt.interactive(False)

plt.grid(b=True,axis='both')
plt.tight_layout()

# PlotManager = plt.get_current_fig_manager()
# PlotManager.window.state('zoomed')

plt.show()
plt.close()