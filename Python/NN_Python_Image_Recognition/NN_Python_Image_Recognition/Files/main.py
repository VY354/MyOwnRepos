
import  time

import matplotlib.image as mpimg

from Work_with_models import *
from Work_with_weights import *
from Work_with_distances import *


# ====================== НАСТРАИВАЕМЫЕ ПАРАМЕТРЫ ======================

SamplesNum = 30000 # объем обучающей выборки (не изменять)
testSize=0.2 # часть тестовой выборки (не изменять)

HiddenLayerSize = 9 # число нейронов в скрытом слое (не изменять)
IterationsNum = 10 # число эпох обучения
NN_Num= 10# количество сетей в популяции
num_of_populations=1

createNew=False # управляющая переменная (не изменять)

Mpath='Models' # папка с обученными моделями (создать папку с таким именем в текущей дериктории при отсутствии)
Dpath='Data' # папка с обучающей выборкой (создать папку с таким именем в текущей дериктории при отсутствии)
Dpath2='Data(shuffle)' # папка с обучающей выборкой (создать папку с таким именем в текущей дериктории при отсутствии)
MWpath='ModelWeights' # папка с весами моделей (создать папку с таким именем в текущей дериктории при отсутствии)
DMPath='DistancesMatrix' # папка с матрицами расстояний (создать папку с таким именем в текущей дериктории при отсутствии)

# ====================================================================


if not os.path.exists(MWpath): os.mkdir(Mpath)
if not os.path.exists(Dpath): os.mkdir(Dpath)
if not os.path.exists(MWpath): os.mkdir(MWpath)
if not os.path.exists(DMPath): os.mkdir(DMPath)


files=0
for _, dirnames, filenames in os.walk(Dpath):
    files += len(filenames)
if files==0:
    X_train, X_test, y_train, y_test = PrepareData(SamplesNum,testSize,False) # создание обучающей и тестовой выборки


# считывание данных обучения и тестирования
X_train = pickle.load(open(Dpath+"\\X_train.txt",'rb'))
X_test = pickle.load(open(Dpath+"\\X_test.txt",'rb'))
y_train = pickle.load(open(Dpath+"\\y_train.txt",'rb'))
y_test = pickle.load(open(Dpath+"\\y_test.txt",'rb'))


StartTime = time.time()

# функция создания и созранения моделей (популяций моделей)
Create_and_Save_Population(ModelsPath=Mpath, # путь сохранения моделей
                           MWpath=MWpath,
                           DMpath=DMPath,
                           HiddenLayerSize=HiddenLayerSize,
                           IterationsNum=IterationsNum,
                           NN_Num=NN_Num,
                           X_train=X_train,
                           y_train=y_train,
                           num_of_population=num_of_populations, # количество популяций
                           growing_iterations='ps',
                           create_new=False) # пересоздать модели (популяции)


#NNs = ReadModels(Mpath) # считывание сохраненных моделей


#функция создания визуализации весов связей
# CreateWeightsImages(MWpath=MWpath, # путь сохранения изображений
#                     HiddenLayerSize=HiddenLayerSize,
#                     NNs=NNs,
#                     X_train=X_train,
#                     X_test=X_test,
#                     y_train=y_train,
#                     y_test=y_test,
#                     create_new=False) # флаг пересоздания изображений

#CreateWeightsGIF(MWpath) # функция создания гифки из изображений весов
#CreateWeigthsProgressionGIF(MWpath) # функция создания гифки прогресии весов (для нескольктх популяций моделей)

#dist = CreateDistanceMatrix(NNs) # функция создания матрицы расстояний
CreateDistancesMatrixImages(DistancesMatrix=dist,
                            DMpath=DMPath,
                            NN_Num=NN_Num,
                            create_new=False)
#CreateDistancesGIF(DMpath=DMPath) # функция создания гифки из матрицы расстояний




#NN = CreateTrainNN(HiddenLayerSize,30,X_train,y_train)









import numpy as np
import pandas as pd


print(type(X_test))




#NN=CreateTrainNN(9,500,X_train,y_train)
#pickle.dump(NN,open(Mpath+'\\'+'Models_1A'+'\\'+'MYNN.sav','wb'))
NN= pickle.load(open(Mpath+'\\'+'Models_1A'+'\\'+'MYNN.sav','rb'))
#CreateWeightsImages(MWpath,9,NN,X_train,X_test,y_train,y_test,True)


PredictOne(NN, X_train, X_test, y_train, y_test)
CreateGIF('Answers')




StopTime = time.time()
deltaTime = StopTime-StartTime
min = time.struct_time(time.gmtime(deltaTime))[4]
sec = time.struct_time(time.gmtime(deltaTime))[5]

print("========================================")
print("Process took {0} min, {1} sec".format(min,sec))
print("========================================")


plt.interactive(False)
plt.show()
plt.close()











