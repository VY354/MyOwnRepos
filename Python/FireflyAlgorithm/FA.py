from math import *
import numpy as np

from dataclasses import dataclass, field, fields, asdict, astuple

import matplotlib.pyplot as plt

from Firefly import Firefly


@dataclass
class FA:
    # function to optimize
    optimizationFunction: object = field(default=None, init=True)
    # optimization problem
    optimizationAction: bool = field(default=True)
    # lower boundary
    lb: float = field(default=0, init=True)
    # upper boundary
    ub: float = field(default=0, init=True)
    # best solution
    __bestSolution: list = field(default_factory=list, init=False)

    # nmber of iterations
    iterationsNumber: int = field(default=100, init=True)
    # number of fireflies
    firefliesQuantity: int = field(default=20, init=True)
    # light absorption coefficient
    gamma: float = field(default=1, init=True)
    # step size coefficient
    alpha: float = field(default=1, init=True)

    # fireflies array
    __fireflies: list = field(default_factory=list, init=False)

    def initialize(self):
        self.conditionFunc = lambda act, x, y: ((x > y) if act else (x < y))

        defaultBrighness = 1
        for i in range(self.firefliesQuantity):
            # set random position within boundary
            pos = np.array(list(map(lambda x: self.lb + x * (self.ub - self.lb), np.random.uniform(-1, 1, 2))))
            self.__fireflies.append(Firefly(pos, defaultBrighness))
        self.__findBestSolution()

    def run(self):
        for i in range(self.iterationsNumber):
            self.iterate()
            self.__findBestSolution()
            print(self.__bestSolution)

    def iterate(self):

        # for each firefly
        # go through all other fireflies
        # if it's brightness higher than curr firefly brightness, than
        # calculate new position with respect to attractiveness of firefly,
        # update current firefly and go to next firefly

        firefly: Firefly
        partner: Firefly
        for firefly in self.__fireflies:
            for partner in [f for f in self.__fireflies if f is not firefly]:
                if self.__compareBrightness(firefly, partner):
                    distance = np.linalg.norm(firefly.position - partner.position)
                    partnerAttrarctiveness = partner.attractiveness * exp(-self.gamma * pow(distance, 2))
                    newPos = firefly.position + partnerAttrarctiveness * (
                            firefly.position - partner.position) + self.alpha * np.random.uniform(-1, 1, 2)
                    firefly.position = newPos
                    newPos = self.__boundPosition(newPos)
                    self.__updateFirefly(firefly, newPos)

        self.__findBestSolution()
        bestFirefly = self.__findBestSolution()
        bestFirefly.position += self.alpha * np.random.uniform(-1, 1, 2)
        bestFirefly.position = self.__boundPosition(bestFirefly.position)

    def __getBrightness(self, position: np.array):

        # compute brightness I as value of objective function
        # there could be different equation for I

        I = self.optimizationFunction(*position)
        return I

    def __compareBrightness(self, firefly: Firefly, partner: Firefly):

        # calculate brightnesses of current and partner fireflies
        # decide brighter it or not

        fireflyBr = self.__getBrightness(firefly.position)
        partnerBr = self.__getBrightness(partner.position)
        return self.conditionFunc(self.optimizationAction, partnerBr, fireflyBr)

    def __updateFirefly(self, firefly: Firefly, newPos: np.array):

        # if newPos brightness greater than previous one,
        # update firefly position and attractiveness

        currBr = self.__getBrightness(firefly.position)
        newBr = self.__getBrightness(newPos)
        if self.conditionFunc(self.optimizationAction, newBr, currBr):
            firefly.position = newPos
            firefly.attractiveness = newBr

    def __findBestSolution(self):
        bestFirefly = self.__fireflies[0]
        bestSolution = [bestFirefly.position, self.optimizationFunction(*bestFirefly.position)]
        for f in self.__fireflies[1:]:
            if self.__compareBrightness(bestFirefly, f):
                bestFirefly = f
                bestSolution = [f.position, self.optimizationFunction(*f.position)]
        self.__bestSolution = bestSolution
        return bestFirefly

    def __boundPosition(self, position: np.array):
        return np.array(
            list(map(lambda x: self.lb if x <= self.lb else (self.ub if x >= self.ub else x), position)))

    def getFirefliesPositions(self):
        return [f.position for f in self.__fireflies]

    def getResult(self):
        return [list(map(lambda x: round(x, 3), self.__bestSolution[0])), round(self.__bestSolution[1], 3)]


def main():
    fa = FA(
        optimizationFunction=lambda x, y: np.cos(x / 2) * np.sin(y / 2),
        optimizationAction=False,
        lb=-2 * pi,
        ub=2 * pi,
        iterationsNumber=100,
        firefliesQuantity=30,
        gamma=0.1,
        alpha=0.05)

    fa.initialize()

    results = []
    itersNum = 200
    for i in range(itersNum):
        fa.iterate()
        res = fa.getResult()
        results.append(res[1])

    fig = plt.figure(figsize=(10, 7), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(range(0, itersNum), results)
    plt.show()


if __name__ == '__main__':
    main()
