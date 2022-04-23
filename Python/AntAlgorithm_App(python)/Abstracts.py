import pygame
from dataclasses import dataclass, field, fields,asdict,astuple
from abc import ABC, abstractmethod, abstractclassmethod



@dataclass()
class Vertex(ABC):
    id: int = field(default=0)



@dataclass()
class Link(ABC):
    vertex0: Vertex = field(default=None)
    vertex1: Vertex = field(default=None)



@dataclass()
class Graph(ABC):
    verticies: list = field(default_factory=list)
    links: list = field(default_factory=list)

    @abstractmethod
    def CreateVerticies(self,number):
        pass

    @abstractmethod
    def setLinksFromExcel(self,ExcelFile,sheetName=0,header=0,index_col=0):
        pass











