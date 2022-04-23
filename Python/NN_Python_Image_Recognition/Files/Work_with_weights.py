

import os

import  time

from PIL import Image
import matplotlib.pyplot as plt

import numpy as np

import inspect

import shutil

from math import *

import Work_with_models
from Work_with_models import *
from Work_with_distances import *





def CreatePlot(subPlotNum,NN,X_train,y_train,X_test, y_test):
    fig, axes = plt.subplots(int(sqrt(subPlotNum)), int(sqrt(subPlotNum)))

    vmin, vmax = NN.coefs_[0].min(), NN.coefs_[0].max()
    coef = NN.coefs_[0].T
    coef = coef.reshape(subPlotNum, 28, 28)

    imgs=[]
    for i in range(subPlotNum):
        imgs.append(axes.ravel()[i].imshow(coef[i],
                               vmin=.5 * vmin,
                               vmax=.5 * vmax,cmap=plt.cm.rainbow))
        axes.ravel()[i].set_xticks(())
        axes.ravel()[i].set_yticks(())

    plt.subplots_adjust(right=0.8)

    cbax = plt.axes([0.85,0.1,0.02,0.8])

    tks=np.arange(-2.0,2.0,0.25)
    fig.colorbar(imgs[0],cbax,axes,orientation='vertical',ticks=tks,format='%.3f')

    TrScore, TsScore = Work_with_models.GetScore(NN,X_train,X_test,y_train,y_test)
    hp = NN.get_params()
    fig.suptitle("Train score = %.3f     |     Test score = %.3f\n  delta = %.3f     |     iterations = %d"%(TrScore,TsScore,TrScore-TsScore,hp.get('max_iter')),fontsize=12)

    return fig, axes



def CreateWeightsImages(MWpath,HiddenLayerSize, NNs, X_train, X_test, y_train, y_test, create_new=False):

    if create_new:
        DeleteWeightsImages(MWpath)

        m=1
        n=0

        if type(NNs) is not list:
            fig, axes = CreatePlot(HiddenLayerSize, NNs, X_train, X_test, y_train, y_test)
            fig.savefig(MWpath + '\\' + "Weigths.png")
            plt.close()

        elif type(NNs[0]) is not list:
            for i in range(len(NNs)):
                if n+65==91:
                    m+=1
                    n=0
                fig, axes = CreatePlot(HiddenLayerSize, NNs[i], X_train, X_test, y_train, y_test)
                fig.savefig(MWpath + '\\' + "Weigths_{0}.png".format(str(m)+chr(65+n)))
                n+=1
                plt.close()

        else:
            m1 = 1
            n1 = 0
            for i in range(len(NNs)):
                if n1 + 65 == 91:
                    m1 += 1
                    n1 = 0
                newMWpath = MWpath+'\\'+'MWpath_{0}'.format(str(m1)+chr(65+n1))
                os.mkdir(newMWpath)
                for j in range(len(NNs[i])):
                    if n + 65 == 91:
                        m += 1
                        n = 0
                    fig, axes = CreatePlot(HiddenLayerSize, NNs[i][j], X_train, X_test, y_train, y_test)
                    fig.savefig(newMWpath + '\\' + "Weigths_{0}.png".format(str(m)+chr(65+n)))
                    n += 1
                    plt.close()
                n1+=1
                n=0
                m=1




def CreateWeightsGIF(MWpath):

    files = folders = 0

    for _, dirnames, filenames in os.walk(MWpath):
        files += len(filenames)
        folders += len(dirnames)

    images = []

    for file in os.listdir(MWpath):
        filename, file_extension = os.path.splitext(MWpath + '\\' + file)
        if file_extension == '.gif':
            os.remove(MWpath + '\\' + file)


    if folders==0:
        for file in os.listdir(MWpath):
            filename, file_extension = os.path.splitext(MWpath + '\\' + file)
            if file_extension == '.gif':
                os.remove(MWpath + '\\' + file)

        for img in os.listdir(MWpath):
            im = Image.open(MWpath + '\\' + img)
            images.append(im)
        images[0].save(MWpath + '\\' + 'Weights_GIF.gif', save_all=True, append_images=images[1:], optimize=False, duration=1000, loop=0)

    else:
        for folder in os.listdir(MWpath):
            for file in os.listdir(MWpath+'\\'+folder):
                filename, file_extension = os.path.splitext(MWpath+'\\'+folder+'\\'+file)
                if file_extension=='.gif':
                    os.remove(MWpath+'\\'+folder+'\\'+file)

        for folder in os.listdir(MWpath):
            images=[]
            for img in os.listdir(MWpath+'\\'+folder):
                im = Image.open(MWpath+'\\'+folder + '\\' + img)
                images.append(im)
            GIFname = MWpath+'\\'+folder+'\\'+'Weights_GIF.gif'
            images[0].save(GIFname, save_all=True, append_images=images[1:], optimize=False, duration=1000,
                           loop=0)




def CreateWeigthsProgressionGIF(MWpath):

    images = []

    filesNum, foldersNum = Count_Folder_File(MWpath)

    for folder in os.listdir(MWpath):
        filename, file_extension = os.path.splitext(folder)
        if file_extension == '.gif':
            os.remove(MWpath + '\\' + folder)

    if foldersNum!=0:
        for folder in os.listdir(MWpath):
            file = random.choice(os.listdir(MWpath+'\\'+folder))
            filename, file_extension = os.path.splitext(file)
            while file_extension=='.gif':
                file = random.choice(os.listdir(MWpath+'\\'+folder))
                filename, file_extension = os.path.splitext(file)
            img = Image.open(MWpath + '\\' + folder + '\\' + file)
            images.append(img)
        images[0].save(MWpath+'\\'+'Weights_Progression_GIF.gif', save_all=True, append_images=images[1:], optimize=False, duration=1000,
                       loop=0)

    pass






def DeleteWeightsImages(MWpath):
    files = folders = 0

    for _, dirnames, filenames in os.walk(MWpath):
        files += len(filenames)
        folders += len(dirnames)

    if folders == 0:
        for img in os.listdir(MWpath):
            os.remove(MWpath+'\\'+img)

    else:
        for folder in os.listdir(MWpath):
            filename, file_extension = os.path.splitext(folder)
            if file_extension == '.gif':
                os.remove(MWpath+'\\'+folder)
            else:
                for img in os.listdir(MWpath+'\\'+folder):
                    os.remove(MWpath+'\\'+folder + '\\' + img)
                os.rmdir(MWpath+'\\'+folder)




def Count_Folder_File(path):
    files = folders = 0

    for _, dirnames, filenames in os.walk(path):
        files += len(filenames)
        folders += len(dirnames)

    return files,folders


def ClearPath(path):
    shutil.rmtree(path,True)
    os.mkdir(path)