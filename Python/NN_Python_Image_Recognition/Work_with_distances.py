

import os

from PIL import Image
import matplotlib.pyplot as plt

import numpy as np

import shutil

from math import *

from sklearn import metrics

from Work_with_models import *





def finddist(NN1,NN2):

    res=0
    coef0=NN1.coefs_[0]
    coef1=NN2.coefs_[0]
    res = sqrt(metrics.mean_squared_error(coef1,coef0)*pow(len(coef0),2))
    return res



def CreateDistanceMatrix(NNs):

    distances = []

    if type(NNs[0]) is not list:
        distances = np.zeros((len(NNs), len(NNs)))
        for i in range(len(NNs)):
            for j in range(len(NNs)):
                distances[i, j] = finddist(NNs[i], NNs[j])
    else:
        for population in  NNs:
            newDistances = np.zeros((len(population), len(population)))
            for i in range(len(population)):
                for j in range(len(population)):
                    newDistances[i, j] = finddist(population[i], population[j])
            distances.append(newDistances)

    return distances



def CreateDistanceMatrixPlot(dist,NN_Num):
    fig, axes = plt.subplots(1)

    avg = sum(dist.ravel())/len(dist.ravel())
    Min=max(dist.ravel())
    for num in dist.ravel():
        if num!=0 and num<Min:
            Min=num
    axes.set(
        title='Distances  |  min =  %.2f  |  max =  %.2f  |  avg = %.2f'%(Min,max(dist.ravel()),avg),
        xticks=np.arange(1, NN_Num + 1),
        yticks=np.arange(1, NN_Num + 1),
    )
    matrix = axes.matshow(dist, cmap=plt.cm.Greens)
    cb = fig.colorbar(matrix)
    return fig,axes



def CreateDistancesMatrixImages(DistancesMatrix,DMpath,NN_Num, create_new=False):

    if create_new:
        DeleteDistancesMatrix(DMpath)

        if type(DistancesMatrix) is not list:
            fig, axes = CreateDistanceMatrixPlot(DistancesMatrix,NN_Num)
            plt.savefig(DMpath+'\\'+'Distances_Matrix.png')
            plt.close()

        else:
            m=1
            n=0
            j = 0
            for i in range(len(DistancesMatrix)):
                if n + 65 == 91:
                    m += 1
                    n = 0
                fig, axes = CreateDistanceMatrixPlot(DistancesMatrix[i],NN_Num)
                plt.savefig(DMpath + '\\' + 'Distances_Matrix_{0}.png'.format(str(m)+chr(65+n)))
                j+=1
                n+=1
                plt.close()
    pass




def CreateDistancesGIF(DMpath):
    images = []

    filesNum, foldersNum = Count_Folder_File(DMpath)

    if filesNum == 1:
        for file in os.listdir(DMpath):
            filename, file_extension = os.path.splitext(file)
            if file_extension == '.gif':
                os.remove(DMpath+'\\'+file)
    else:
        for img in os.listdir(DMpath):
            im = Image.open(DMpath + '\\' + img)
            images.append(im)
        images[0].save(DMpath+'\\'+'Distances_Matrix_GIF.gif', save_all=True, append_images=images[1:], optimize=False, duration=1000,
                       loop=0)



def DeleteDistancesMatrix(DMpath):
    files = folders = 0

    for _, dirnames, filenames in os.walk(DMpath):
        files += len(filenames)
        folders += len(dirnames)

    if folders == 0:
        for img in os.listdir(DMpath):
            os.remove(DMpath + '\\' + img)

    else:
        for folder in os.listdir(DMpath):
            for img in os.listdir(DMpath + '\\' + folder):
                os.remove(DMpath + '\\' + folder + '\\' + img)
            os.rmdir(DMpath + '\\' + folder)




def Count_Folder_File(path):
    files = folders = 0

    for _, dirnames, filenames in os.walk(path):
        files += len(filenames)
        folders += len(dirnames)

    return files,folders