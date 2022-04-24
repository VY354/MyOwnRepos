import pygame
from dataclasses import dataclass, field, fields,asdict,astuple
from abc import ABC, abstractmethod, abstractclassmethod

import numpy as np

from Abstracts import *
from Interfaces import *
from Functions import *

pygame.init()


@dataclass(init=False)
class RectObj:

    rect : pygame.Rect

    def __init__(self):
        self.rect = pygame.Rect((0,0),(0,0))

    def setRect(self,newRect):
        self.rect=newRect

    def setTopLeft(self,newTopLeftPos):
        self.rect.topleft=newTopLeftPos
    def getTopLeft(self):
        return self.rect.topleft

    def setBottomRight(self,newBottomRight):
        self.rect.bottomright=newBottomRight
    def getBottomRight(self):
        return self.rect.bottomright

    def setCenter(self,newCenter):
        self.rect.center=newCenter
    def getCenter(self):
        return self.rect.center

    def setSize(self,newSize):
        self.rect.size=newSize
    def getSize(self):
        return self.rect.size



@dataclass()
class UIObj:
    rectObj: RectObj = field(default=RectObj())
    shapeData: object = field(default=None)

    def __init__(self):
        self.rectObj=RectObj()
        self.shapeData = object()




@dataclass()
class CircleData:

    center : tuple
    radius : int
    color: tuple
    width: int

    def __init__(self,center=(0,0),radius=15,color=(255,255,255),width=False):
        self.center=center
        self.radius=radius
        self.color=color
        self.width=width



@dataclass()
class LineData:

    start : tuple
    end : tuple
    color : list
    width : int

    def __init__(self,start=(0,0),end=(0,0),color=(200,200,200),width=2):
        self.start=start
        self.end=end
        self.color=color
        self.width=width



@dataclass()
class TextData:

    pos : tuple = field(default=(0,0))
    surf : pygame.Surface = field(default=pygame.Surface((0,0)))
    fontObj : pygame.font.SysFont = field(default=pygame.font.SysFont('arial',15))
    text : str = field(default='NONE')
    color : tuple = field(default=(255,255,255))
    bgcolor : object = field(default=False)

    def setFontSize(self,newSize):
        self.fontObj = pygame.font.SysFont('arial',newSize)



class CircleUIObj(UIObj,IDrawable,IMovable):

    def __init__(self):
        super().__init__()
        self.shapeData: CircleData = CircleData()
        self.rectObj.setCenter(self.shapeData.center)
        self.rectObj.setSize((self.shapeData.radius*2,self.shapeData.radius*2))


    def Draw(self,surface : pygame.Surface):
        pygame.draw.circle(
            surface=surface,
            center=self.shapeData.center,
            radius=self.shapeData.radius,
            width=self.shapeData.width,
            color=self.shapeData.color
        )

    def Move(self, relative : tuple):
        self.rectObj.rect.move_ip(relative)
        self.shapeData.center=self.rectObj.rect.center

    def setCenter(self,newCenter):
        self.rectObj.rect.center=newCenter
        self.shapeData.center = self.rectObj.rect.center



@dataclass()
class LineUIObj(UIObj,IDrawable):

    def __init__(self):
        self.shapeData : LineData = LineData()
        w = abs(self.shapeData.end[0]-self.shapeData.start[0])
        l = abs(self.shapeData.end[1] - self.shapeData.start[1])
        self.rectObj.setTopLeft(self.shapeData.start)
        self.rectObj.setSize((l,w))

    def Draw(self,surface):
        pygame.draw.line(
                surface=surface,
                start_pos=self.shapeData.start,
                end_pos=self.shapeData.end,
                width=self.shapeData.width,
                color=self.shapeData.color
            )

    def setStart(self,start):
        self.rectObj.setTopLeft(start)
        self.shapeData.start=start

    def setEnd(self,end):
        self.rectObj.setBottomRight(end)
        self.shapeData.end = end

    def setStartEnd(self,start,end):
        self.rectObj.setTopLeft(start)
        self.rectObj.setBottomRight(end)
        self.shapeData.start = start
        self.shapeData.end = end


@dataclass()
class TextUIObj(UIObj,IDrawable):

    def __init__(self):
        super().__init__()
        self.shapeData : TextData = TextData()


    def Draw(self, surface : pygame.Surface):
        self.shapeData.surf = self.shapeData.fontObj.render(str(self.shapeData.text),False,self.shapeData.color,self.shapeData.bgcolor)
        self.rectObj.setRect(self.shapeData.surf.get_rect())
        self.rectObj.setCenter(self.shapeData.pos)
        surface.blit(self.shapeData.surf,self.rectObj.rect)








def RectObjClassCheck():
    print('\n================== RECT CHECK ==================\n')

    r1 = RectObj()
    r2 = RectObj()

    r1.setCenter((100, 100))
    r2.setCenter((200, 200))


    print(f'{asdict(r1)}')
    print(f'{asdict(r2)}')


def CircleDataClassCheck():
    print('\n================== CIRCLE DATA CHECK ==================\n')

    cd = CircleData((100,100),25,(10,20,30),5)
    print(asdict(cd))


def LineDataClassCheck():
    print('\n================== LINE DATA CHECK ==================\n')

    ld = LineData((10,10),(100,100),(1,2,3),7)
    print(asdict(ld))


def CircleUIObjClassCheck():
    print('\n================== CIRCLE UI OBJ CHECK ==================\n')

    vuiobj1 = CircleUIObj()
    vuiobj2 = CircleUIObj()

    print(f'{asdict(vuiobj1)=}')
    print(f'{asdict(vuiobj2)=}')

    vuiobj1.Move((100,100))

    print(f'{asdict(vuiobj1)=}')
    print(f'{asdict(vuiobj2)=}')

    vuiobj2.Move((200,200))

    print(f'{asdict(vuiobj1)=}')
    print(f'{asdict(vuiobj2)=}')


def LineUIObjClassCheck():
    print('\n================== LINE UI OBJ CHECK ==================\n')

    luiobj =LineData()
    print(f'{luiobj=}')


def TextUIObjClassCheck():
    print('\n================== TEXT UI OBJ CHECK ==================\n')

    tuiobj = TextUIObj()
    print(f'{tuiobj=}')





if __name__ == '__main__':
    RectObjClassCheck()
    CircleDataClassCheck()
    LineDataClassCheck()
    CircleUIObjClassCheck()
    LineUIObjClassCheck()
    TextUIObjClassCheck()












