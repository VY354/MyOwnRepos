import random
import numpy as np
from dataclasses import dataclass
from abc import ABC, abstractmethod

from Graph2d import *


@dataclass()
class Path:
    link: Link
    FeromoneValue: int
    FeromoneAmountToAdd: int

    def __init__(self, vertex0, vertex1, weight):
        self.link = Link(vertex0, vertex1, weight)
        self.FeromoneValue = 0
        self.FeromoneAmountToAdd = 0

    def __eq__(self, other):
        return (self.link.vertex0 == other.link.vertex0 and self.link.vertex1 == other.link.vertex1)

    def __ne__(self, other):
        return (self.link.vertex0 != other.link.vertex0 and self.link.vertex1 != other.link.vertex1)


@dataclass()
class Ant:
    StartVertexIndex: int
    AntPath: list


class AntAlgorithm:

    def __init__(self,
                 num_of_vertex=1,
                 num_of_ants=1,
                 num_of_iterations=1,
                 weight_constant=1,
                 q_constant=1,
                 weight_priority_factor=1,
                 feromone_priority_factor=1,
                 feromone_remain_precentage=1,
                 path_default_feromone=1,
                 default_delta_feromone=1
                 ):
        # graph properties
        self._Num_of_vertex = num_of_vertex
        self._Graph = Graph()
        self._Graph.CreateVerticies(num_of_vertex)

        # paths variables
        self.Default_feromone_value = path_default_feromone
        self._WalkedPaths = []
        self._TotalPath = []
        self._TotalLength = -1

        # ants and iterations parameters
        self._NumOfAnts = num_of_ants
        self._Ants = []
        self.DefaultDeltaFeromone = default_delta_feromone

        # algorithm parameters
        self.NumOfIterations = num_of_iterations
        self.WeightConstant = weight_constant
        self.QConstant = q_constant
        self.FeromoneRemainPrecentage = feromone_remain_precentage

        # ants property orientation
        self.WeightPriorityFactor = weight_priority_factor
        self.FeromonePriorityFactor = feromone_priority_factor


if __name__ == '__main__':
    alg = AntAlgorithm()
