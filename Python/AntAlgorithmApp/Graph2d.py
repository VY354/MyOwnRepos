import random
import numpy as np
import pandas as pd
import pygame
from dataclasses import dataclass, field, fields,asdict,astuple
from abc import ABC, abstractmethod, abstractclassmethod


from Abstracts import *


def idGenerator():
    id=0
    while 1:
        yield id
        id+=1
idGen=idGenerator()



@dataclass()
class Point2d:
    x: float = 0
    y: float = 0

    def getNpArr(self):
        return np.array([self.x,self.y])

    def setPos(self,newPos):
        self.x,self.y=newPos



@dataclass()
class Vertex2d(Vertex):

    pos : Point2d = field(default_factory=Point2d)

    def __init__(self,pos = (0,0)):
        self.pos=Point2d(*pos)
        self.id=next(idGen)

    def getPosNpArr(self):
        return self.pos.getNpArr()

    def setPos(self,newPos : tuple):
        self.pos.setPos(newPos)



@dataclass()
class Link2d(Link):

    weight : float = field(default=0)
    vertex0 : Vertex2d = field(default_factory=Vertex2d)
    vertex1 : Vertex2d = field(default_factory=Vertex2d)

    def __init__(self,v0:Vertex2d=None,v1:Vertex2d=None,weight=0):
        self.vertex0=v0
        self.vertex1=v1
        self.weight=weight



@dataclass(init=False,order=False,eq=False)
class Graph2d(Graph):

    def CreateVerticies(self,number):
        for i in range(number):
            v=Vertex2d()
            v.id=i
            self.verticies.append(v)

    def setVerticiesPosFromExcel(self,ExcelFile,sheetName=0,header=0,index_col=0):
        posArr = np.array(pd.read_excel(ExcelFile,sheet_name=sheetName,header=header,index_col=index_col))
        v:Vertex2d
        for v,pos in zip(self.verticies,posArr):
            v.setPos(tuple(pos))

    def setVerticiesPosRandom(self, xmin,ymin,xmax,ymax):
        for v in self.verticies:
            x=random.randint(xmin,xmax)
            y=random.randint(ymin,ymax)
            v.setPos((x,y))

    def setLinksFromExcel(self,ExcelFile,sheetName=0,header=0,index_col=0):
        adjacencyMatrix = np.array(pd.read_excel(ExcelFile, sheet_name=sheetName, header=header, index_col=index_col))
        self.links=[]
        for i in range(adjacencyMatrix.shape[0]):
            row=[]
            for j in range(adjacencyMatrix.shape[1]):
                if adjacencyMatrix[i,j]==1:
                    row.append(Link2d(self.verticies[i],self.verticies[j]))
            self.links.append(row)

    def setWeightsFromExcel(self, ExcelFile, sheetName=0, header=0, index_col=0):
        weights = np.array(pd.read_excel(ExcelFile, sheet_name=sheetName, header=header, index_col=index_col))
        for i in range(weights.shape[0]):
            for j in range(weights.shape[1]):
                self.links[i][j].weight=weights[i,j]

    def setWeightsToValue(self, value):
        for row in self.links:
            for l in row:
                l.weight=value





if __name__ == '__main__':

    g = Graph2d()
    print(f'{asdict(g)=}')

    g.CreateVerticies(3)
    print(f'{asdict(g)=}')

    print('====================================================')
    g.setVerticiesPosRandom(0,0,200,200)
    for v in g.verticies:
        print(f'{v=}')

    print('====================================================')
    g.setVerticiesPosFromExcel(f'F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\AntAlgorithm\graph.xlsx',0)
    for v in g.verticies:
        print(f'{v=}')

    print('====================================================')
    g.setLinksFromExcel(f'F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\AntAlgorithm\graph.xlsx',1)
    for row in g.links:
        for l in row:
            print(f'{astuple(l)=}')

    print('====================================================')
    g.setWeightsToValue(100)
    for row in g.links:
        for l in row:
            print(f'{astuple(l)=}')

    print('====================================================')
    g.setWeightsFromExcel(f'F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\AntAlgorithm\graph.xlsx', 2)
    for row in g.links:
        for l in row:
            print(f'{astuple(l)=}')




# alpha = atan(self.line_obj.rect.height / self.line_obj.rect.width) * 180 / pi
# pos = (np.array([self.line_obj.rect.centerx, self.line_obj.rect.centery]) + np.array(
# [10 * tan(-alpha), -10])).astype('int')


