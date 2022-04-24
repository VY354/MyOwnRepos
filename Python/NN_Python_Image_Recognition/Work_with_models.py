

import os

import  time

import random

from  copy import  copy

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

import pickle

import glob
import shutil

from Work_with_distances import *
from Work_with_weights import *




def PrepareData(SamplesNum,testSize,doShuffle=False):
    X, y = fetch_openml(
        'mnist_784',
        version=1,
        return_X_y=True)

    X = X / 255.

    return train_test_split(
        X[:SamplesNum], y[:SamplesNum],
        test_size=testSize,
        shuffle=doShuffle)



def SaveModels(NNs,ModelsPath):
    m=1
    n=0
    for i in range(len(NNs)):
        if n+65==91:
            m+=1
            n=0
        filename=ModelsPath+'\\'+'model_{0}.sav'.format(str(m)+chr(65+n))
        n+=1
        pickle.dump(NNs[i],open(filename,'wb'))



def ReadModels(ModelsPath):

    files = folders = 0

    for _, dirnames, filenames in os.walk(ModelsPath):
        files += len(filenames)
        folders += len(dirnames)

    NNs = []

    if folders==0:
        for model in sorted(os.listdir(ModelsPath)):
            NNs.append(pickle.load(open(ModelsPath + '\\' + model, 'rb')))

    else:
        for folder in sorted(os.listdir(ModelsPath)):
            newNNs=[]
            for model in sorted(os.listdir(ModelsPath+'\\'+folder)):
                newNNs.append(pickle.load(open(ModelsPath+'\\'+folder+'\\'+model,'rb')))
            NNs.append(newNNs)

    return NNs




def DeleteModels(ModelsPath):

    files = folders = 0

    for _, dirnames, filenames in os.walk(ModelsPath):
        files += len(filenames)
        folders += len(dirnames)

    if folders==0:
        for model in os.listdir(ModelsPath):
            os.remove(ModelsPath + '\\' + model)

    else:
        for folder in os.listdir(ModelsPath):
            for model in os.listdir(ModelsPath+'\\'+folder):
                os.remove(ModelsPath+'\\'+folder+'\\'+model)
            os.rmdir(ModelsPath+'\\'+folder)



def CreateTrainNN(subPlotNum,IterationsNum,X_train,y_train):
    Layers=(subPlotNum,)
    NN = MLPClassifier(hidden_layer_sizes=Layers,
                       activation='logistic',
                       max_iter=IterationsNum,
                       alpha=1e-4,
                       solver='sgd',
                       verbose=10,
                       random_state=int((random.randint(1,100000)+random.randint(1,100000))/2),
                       learning_rate_init=.1,
                       shuffle=False)

    NN.fit(X_train, y_train)
    return NN



def CreatePopulation(subPlotNum,IterationsNum,NN_Num,X_train,y_train,growing_iterations=False):
    NNs=[]

    iter=IterationsNum
    if growing_iterations==True: iter=1

    for i in range(NN_Num):
        NNs.append(CreateTrainNN(subPlotNum, iter, X_train, y_train))
        if growing_iterations==True: iter+=1
    return NNs



def Create_and_Save_Population(ModelsPath, MWpath, DMpath, HiddenLayerSize, IterationsNum, NN_Num, X_train, y_train, num_of_population=1, growing_iterations='ps',create_new=False):

    if create_new:
        DeleteModels(ModelsPath)
        DeleteDistancesMatrix(DMpath)
        DeleteWeightsImages(MWpath)

        NNs = []


        m=1
        n=0

        for p in range(num_of_population):

            if n + 65 == 91:
                m += 1
                n = 0

            if growing_iterations=='ps' and num_of_population>1:
                NNs = CreatePopulation(HiddenLayerSize, p+1, NN_Num, X_train, y_train,False)
            elif growing_iterations=='p':
                NNs = CreatePopulation(HiddenLayerSize, IterationsNum, NN_Num, X_train, y_train, True)
            else:
                NNs = CreatePopulation(HiddenLayerSize, IterationsNum, NN_Num, X_train, y_train, False)

            NewModelsPath = ModelsPath + '\\' + 'Models_{0}'.format(str(m)+chr(65+n))
            os.mkdir(NewModelsPath)
            SaveModels(NNs, NewModelsPath)

            n+=1


def GetScore(NN,X_train,X_test,y_train,y_test):
    TrainScore = NN.score(X_train, X_test)
    TestScore = NN.score(y_train, y_test)
    return TrainScore, TestScore



def ShowAccuracy(NN,X_train,y_train,X_test, y_test):
    TrAcc, TsAcc = GetScore(NN,X_train,y_train,X_test, y_test)
    print("\n==============================================\n")
    print(NN)
    print("Training accuracy = %f\n" % TrAcc)
    print("Testing accuracy = %f" % TsAcc)
    print("\n==============================================\n")


def PredictOne(NN, X_train, X_test, y_train, y_test):


    actual_pict = X_test.to_numpy()[3167]
    noised_pict = copy(actual_pict)


    n = 0
    for k in range(1,6):
        count=0
        for i in range(len(noised_pict)):
            rnd = random.randint(0,100)
            if rnd < k*5:
                count+=1
                noised_pict[i]=random.uniform(0,1)

        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2)

        ax1.matshow(actual_pict.reshape(28, 28), cmap=plt.cm.gray)
        ax2.matshow(noised_pict.reshape(28, 28), cmap=plt.cm.gray)

        fig.tight_layout()

        actual_predict = NN.predict(actual_pict.reshape(1,-1))
        noised_predict = NN.predict(noised_pict.reshape(1,-1))

        ax1.set_title("Actual image     |     Net answer = %d" % (int(actual_predict[0])), fontsize=14)
        ax2.set_title("Noised: %.2f %%     |     Net answer = %d" % (count/784*100,int(noised_predict[0])), fontsize=14)

        ax1.set_xticks(())
        ax1.set_yticks(())

        ax2.set_xticks(())
        ax2.set_yticks(())


        fig.savefig("Answers" + '\\' + "Weigths_{0}.png".format(chr(65+n)))
        n+=1

        plt.close()





def CreateGIF(Path):
    images = []
    for img in os.listdir(Path):
        im = Image.open(Path + '\\' + img)
        images.append(im)
    GIFname = Path + '\\' + 'Weights_GIF.gif'
    images[0].save(GIFname, save_all=True, append_images=images[1:], optimize=False, duration=1500,
                   loop=0)






