import pygame
from dataclasses import dataclass, field, fields
from abc import ABC, abstractmethod, abstractclassmethod



class IDrawable(ABC):
    @abstractmethod
    def Draw(self,*args,**kwargs):
        pass



class IMovable(ABC):
    @abstractmethod
    def Move(self, *args, **kwargs):
        pass



class IGraph(ABC):
    @abstractmethod
    def CreateVerticies(self,num):
        pass







