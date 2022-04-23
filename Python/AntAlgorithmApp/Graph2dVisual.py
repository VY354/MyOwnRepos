import pygame
from dataclasses import dataclass, field, fields, asdict, astuple
from abc import ABC, abstractmethod, abstractclassmethod
from typing import List, Tuple, Dict

from Graph2d import *
from UIClasses import *


@dataclass()
class Graph2dVisual(Graph2d, IDrawable):
    VerticiesUIObjs: List[CircleUIObj] = field(default_factory=list)
    LinksUIObjs: List[LineUIObj] = field(default_factory=list)
    VerticiesLabelsUIObjs: List[TextUIObj] = field(default_factory=list)
    LinksLabelsUIObjs: List[TextUIObj] = field(default_factory=list)

    def initVUIObjs(self):
        v: Vertex2d
        for v in self.verticies:
            vuiobj = CircleUIObj()
            vuiobj.setCenter(v.pos.getNpArr())
            self.VerticiesUIObjs.append(vuiobj)

    def updVUIObjs(self):
        v: Vertex2d
        for v, vUI in zip(self.verticies, self.VerticiesUIObjs):
            vUI.setCenter(v.pos.getNpArr())

    def initLUIObjs(self):
        for row in self.links:
            l: Link2d
            rowLUI = []
            for l in row:
                luiobj = LineUIObj()
                luiobj.setStart(l.vertex0.pos.getNpArr())
                luiobj.setEnd(l.vertex1.pos.getNpArr())
                rowLUI.append(luiobj)
            self.LinksUIObjs.append(rowLUI)

    def updLUIObjs(self):
        l: Link2d
        for rowl, rowlUI in zip(self.links, self.LinksUIObjs):
            for l, lUI in zip(rowl, rowlUI):
                lUI.setStart(l.vertex0.pos.getNpArr())
                lUI.setEnd(l.vertex1.pos.getNpArr())

    def initVTUIObjs(self):
        v: Vertex2d
        for v in self.verticies:
            label = TextUIObj()
            label.shapeData.setFontSize(20)
            label.shapeData.color = (0, 0, 0)
            label.shapeData.text = v.id
            label.shapeData.bgcolor = (255, 255, 255)
            self.VerticiesLabelsUIObjs.append(label)

    def updVTUIObjs(self):
        v: Vertex2d
        t: TextUIObj
        for v, t in zip(self.verticies, self.VerticiesLabelsUIObjs):
            t.shapeData.pos = v.pos.getNpArr()

    def initLTUIObjs(self):
        l: Link2d
        for row in self.links:
            rowLabels = []
            for l in row:
                label = TextUIObj()
                label.shapeData.setFontSize(20)
                label.shapeData.color = (255, 255, 255)
                label.shapeData.text = l.weight
                label.shapeData.bgcolor = (150, 150, 150)
                rowLabels.append(label)
            self.LinksLabelsUIObjs.append(rowLabels)

    def updLTUIObjs(self):
        linkUI: LineUIObj
        label: TextUIObj
        for rowLinkUI, rowLinkLabel in zip(self.LinksUIObjs, self.LinksLabelsUIObjs):
            for linkUI, linklabel in zip(rowLinkUI, rowLinkLabel):
                linklabel.shapeData.pos = (linkUI.rectObj.rect.centerx, linkUI.rectObj.rect.centery)


    def updVertex(self, v2d: Vertex2d, v2dUI: CircleUIObj, rel):
        v2dUI.Move(rel)
        v2d.setPos(v2dUI.rectObj.getCenter())

    def FindSelectedVertex(self, mousePos):
        for v, vUI in zip(self.verticies, self.VerticiesUIObjs):
            if vUI.rectObj.rect.collidepoint(mousePos):
                return v, vUI
        return None, None

    def init(self):
        self.initVUIObjs()
        self.initLUIObjs()
        self.initVTUIObjs()
        # self.initLTUIObjs()

    def upd(self):
        self.updVUIObjs()
        self.updLUIObjs()
        self.updVTUIObjs()
        # self.updLTUIObjs()

    def Draw(self, surface):
        for rowlUI in self.LinksUIObjs:
            for lUI in rowlUI:
                lUI.Draw(surface)

        for vUI in self.VerticiesUIObjs:
            vUI.Draw(surface)

        for vtUI in self.VerticiesLabelsUIObjs:
            vtUI.Draw(surface)

        # for rowUI in self.LinksLabelsUIObjs:
        #     for ltUI in rowUI:
        #         ltUI.Draw(surface)





if __name__ == '__main__':
    g2dv = Graph2dVisual()
    print(f'{asdict(g2dv)=}')

    g2dv.CreateVerticies(2)
    g2dv.setVerticiesPosFromExcel(f'F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\AntAlgorithm\graph.xlsx',
                                  0)
    print(f'{asdict(g2dv)=}')

    g2dv.initVUIObjs()
    g2dv.updVUIObjs()
    print(f'{asdict(g2dv)=}')

    g2dv.setLinksFromExcel(f'F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\AntAlgorithm\graph.xlsx', 1)
    g2dv.initLUIObjs()
    g2dv.updLUIObjs()
    print(f'{asdict(g2dv)=}')

    g2dv.upd()
