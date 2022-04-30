from math import *
import random

import dataclasses
from dataclasses import dataclass, field, fields, asdict, astuple

import numpy as np

from Particle import Particle


@dataclass
class PSO:
    # function to evaluate parameters
    objectiveFunction: object = field(default=None, init=True)
    optimizationAction: bool = field(default=True, init=True)
    lb: float = field(default=0, init=True)
    ub: float = field(default=0, init=True)

    # result parameters
    _resultPos: np.array = field(default=np.array([0, 0], dtype='float64'), init=False)
    _resultValue: float = field(default=0, init=False)

    maxIterations: int = field(default=100)

    # agents parameters
    _particles: list = field(default=None, init=False)
    particleQuantity: int = field(default=20, init=True)
    inertia: float = field(default=1, init=True)
    personalComponent: float = field(default=1, init=True)
    groupComponent: float = field(default=1, init=True)

    def Initialize(self):
        self.conditionFunc = lambda act, x, y: ((x > y) if act else (x < y))
        self._particles = [Particle() for i in range(self.particleQuantity)]
        p: Particle

        # creating agents population;
        # set random position, velocity and best results
        for p in self._particles:
            p.position = np.random.uniform(random.uniform(self.lb, self.ub), random.uniform(self.lb, self.ub), 2)
            p.velocity = np.random.uniform(-1, 1, 2)
            p.personalBestValue = self.objectiveFunction(*p.position)
            p.personalBestPosition = p.position

    def Run(self):
        for i in range(self.maxIterations):
            self._Iterate()

    def _Iterate(self):
        p: Particle
        # get best position at current state
        groupBestPos = self._GetGroupBest()
        # for each particle update its velocity and personal best
        for p in self._particles:
            # update rule: v_new = w * v_curr + c1 * r1 * (PB - X_curr) + c2 * r2 * (GB - X_curr), where:
            # v_new - new velocity
            # v_curr - current velocity
            # X_curr - current position
            # w - velocity inertia component coefficient
            # c1, c2 - personal best and group best components coefficients
            # r1, r2 - random float between 0 and 1
            p.velocity = self.inertia * p.velocity + self.personalComponent * random.random() * (
                    p.personalBestPosition - p.position) + self.groupComponent * random.random() * (
                                 groupBestPos - p.position)
            p.position = p.position + p.velocity
            p.position = np.array(list(map((lambda x: self.lb if x <= self.lb else (
                self.ub if x >= self.ub else x)), p.position)))
            self.UpdatePB(p)

        # update results on current iteration
        self._resultPos, self._resultValue = self.GetBestResultPos()

    def _GetGroupBest(self) -> np.array:
        bestPos = self._particles[0].position
        fbest = self.objectiveFunction(*bestPos)

        # finding best position by comparison all agents values
        for p in self._particles[1:]:
            if self.conditionFunc(self.optimizationAction, p.personalBestValue, fbest):
                fbest = p.personalBestValue
                bestPos = p.personalBestPosition
        return bestPos

    def UpdatePB(self, p: Particle):
        # update personal bests depending on maximizing or minimizing function
        funcVal = self.objectiveFunction(*p.position)
        if self.conditionFunc(self.optimizationAction, p.personalBestValue, funcVal):
            p.personalBestValue = funcVal
            p.personalBestPosition = p.position

    def GetBestResultPos(self):
        # get average agents position and average result
        poses = np.array([p.position for p in self._particles])
        avgPos = np.sum(poses, axis=0) / len(self._particles)
        avgRes = self.objectiveFunction(*avgPos)
        return avgPos, avgRes

    def GetParticlesPositions(self):
        return [p.position for p in self._particles]

    def GetResult(self):
        return (self._resultPos, self._resultValue)


def test():
    pso = PSO()

    pso.objectiveFunction = lambda x, y: np.cos(x) * np.sin(y)
    pso.optimizationAction = False
    pso.lb = -2 * pi
    pso.ub = 2 * pi

    pso.maxIterations = 100
    pso.particleQuantity = 30

    pso.inertia = 0.05
    pso.personalComponent = 0.2
    pso.groupComponent = 1

    pso.Initialize()
    pso.Run()

    print(pso._resultPos, pso._resultValue)


if __name__ == '__main__':
    test()
