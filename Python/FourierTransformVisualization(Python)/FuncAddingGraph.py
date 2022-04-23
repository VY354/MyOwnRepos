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

def getFuncList(alpha,amplitudeList,freqList,phaseList):
    funcList=[]
    funcList.append([0])
    for i in range(len(amplitudeList)):
        f = amplitudeList[i]*np.sin(freqList[i]*alpha+phaseList[i])
        funcList.append(f)
    f=np.zeros((len(alpha)))
    for i in range(1,len(funcList)):
        f+=funcList[i]
    funcList[0]= f
    return funcList

# ===============================================================================

plotsNum=3+1

fig = plt.figure(figsize=(12, 7))

axesList=[]
for i in range(plotsNum):
    ax = fig.add_subplot(plotsNum,1,i+1)
    axesList.append(ax)

# ===============================================================================

minA=0
maxA=4*pi
dA=0.01
alpha = np.arange(minA,maxA,dA)

amplitudeList = np.array([1,1,1])
freqList = np.array([2,5,9])*1
phaseList = np.array([0,0,0])

# amplitudeList = [i for i in range(plotsNum)]
# freqList = [i*10 for i in range(plotsNum)]
# phaseList = [0 for i in range(plotsNum)]

plots=getFuncList(alpha,amplitudeList,freqList,phaseList)

# ===============================================================================

offset1=1
mnx = alpha.min() - offset1/2
mxx = alpha.max() + offset1/2
mny = plots[0].min() - offset1
mxy = plots[0].max() + offset1

# ===============================================================================

for ax in axesList:
    ax.set_xlim(mnx,mxx)
    ax.set_ylim(mny,mxy)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

# ===============================================================================

dCLR=255/(len(plots))
CLR=dCLR
for (ax,p) in zip(axesList,plots):
    ax.plot(alpha,p,lw='2',ls='-',c=matplotlib.colors.to_rgb((0,1-CLR/255,0)))
    CLR+=dCLR

# ===============================================================================
# ===============================================================================

#plt.savefig(fname = r"F:\From Disk Windows 7 SSD\Home Work\Different\Essence of Fourier Transform\Images\FuncAdd(1).png", dpi=100)

# ===============================================================================

plt.interactive(False)
plt.tight_layout()

# PlotManager = plt.get_current_fig_manager()
# PlotManager.window.state('zoomed')

plt.show()
plt.close()

