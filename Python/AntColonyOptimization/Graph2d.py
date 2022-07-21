import random
import numpy as np
import pandas as pd

from dataclasses import dataclass, field, fields, asdict, astuple
from abc import ABC, abstractmethod, abstractclassmethod

from Abstracts import *


def idGenerator():
    id = 0
    while 1:
        yield id
        id += 1


idGen = idGenerator()


@dataclass()
class Point2d:
    x: float = 0
    y: float = 0

    def getPosition(self):
        return np.array([self.x, self.y])

    def setPosition(self, newPos):
        self.x, self.y = newPos


@dataclass()
class Vertex2d(Vertex):
    position: Point2d = field(default_factory=Point2d)

    def __init__(self, position=(0, 0)):
        self.position = Point2d(*position)
        self.id = next(idGen)

    def getPosition(self):
        return self.position.getPosition()

    def setPosition(self, newPos: tuple):
        self.position.setPosition(newPos)


@dataclass()
class Link2d(Link):
    weight: float = field(default=0)
    vertex0: Vertex2d = field(default_factory=Vertex2d)
    vertex1: Vertex2d = field(default_factory=Vertex2d)

    def __init__(self, v0: Vertex2d = None, v1: Vertex2d = None, weight=0):
        self.vertex0 = v0
        self.vertex1 = v1
        self.weight = weight


@dataclass(init=False, order=False, eq=False)
class Graph2d(Graph):

    def CreateVerticies(self, number):
        for i in range(number):
            v = Vertex2d()
            v.id = i
            self.verticies.append(v)

    def setVertPosFromExcel(self, ExcelFile, sheetName=0, header=0, index_col=0):
        posArr = np.array(pd.read_excel(ExcelFile, sheet_name=sheetName, header=header, index_col=index_col))
        v: Vertex2d
        for v, position in zip(self.verticies, posArr):
            v.setPosition(tuple(position))

    def setVertPosRandom(self, xmin, ymin, xmax, ymax):
        v: Vertex2d
        for v in self.verticies:
            x = random.randint(xmin, xmax)
            y = random.randint(ymin, ymax)
            v.setPosition((x, y))

    def setLinksFromExcel(self, ExcelFile, sheetName=0, header=0, index_col=0):
        adjacencyMatrix = np.array(pd.read_excel(ExcelFile, sheet_name=sheetName, header=header, index_col=index_col))
        self.links = []
        for i in range(adjacencyMatrix.shape[0]):
            row = []
            for j in range(adjacencyMatrix.shape[1]):
                if adjacencyMatrix[i, j] == 1:
                    row.append(Link2d(self.verticies[i], self.verticies[j]))
            self.links.append(row)

    def setWeightsFromExcel(self, ExcelFile, sheetName=0, header=0, index_col=0):
        weights = np.array(pd.read_excel(ExcelFile, sheet_name=sheetName, header=header, index_col=index_col))
        for i in range(weights.shape[0]):
            for j in range(weights.shape[1]):
                self.links[i][j].weight = weights[i, j]

    def setWeightsToValue(self, value):
        for row in self.links:
            for l in row:
                l.weight = value


if __name__ == '__main__':

    g = Graph2d()
    print(f'{asdict(g)=}')

    g.CreateVerticies(3)
    print(f'{asdict(g)=}')

    print('====================================================')
    g.setVertPosRandom(0, 0, 200, 200)
    for v in g.verticies:
        print(f'{v=}')

    print('====================================================')
    g.setVertPosFromExcel(f'/home/rayxxx/LinksToFolders/PythonProjects/SwarmIntelligenceProjects/AntColonyOptimization/graph.xlsx', 0)
    for v in g.verticies:
        print(f'{v=}')

    print('====================================================')
    g.setLinksFromExcel(f'/home/rayxxx/LinksToFolders/PythonProjects/SwarmIntelligenceProjects/AntColonyOptimization/graph.xlsx', 1)
    for row in g.links:
        for l in row:
            print(f'{astuple(l)=}')

    print('====================================================')
    g.setWeightsToValue(100)
    for row in g.links:
        for l in row:
            print(f'{astuple(l)=}')

    print('====================================================')
    g.setWeightsFromExcel(f'/home/rayxxx/LinksToFolders/PythonProjects/SwarmIntelligenceProjects/AntColonyOptimization/graph.xlsx', 2)
    for row in g.links:
        for l in row:
            print(f'{astuple(l)=}')
