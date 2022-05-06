from math import *
import random
import numpy as np

from dataclasses import dataclass, field, fields, asdict, astuple

import matplotlib.pyplot as plt

from Particle import Particle

"""

concept idea:

1. for each particle:
    look around and choose the best direction to move
    it will show where to move

2. get best solution

3. for each particle:
    update position with rule:
    x_new = x_old + moveDirCoeff * x_moveDir + gbCoeff * bestRating * (x_old - x_best) + randCoeff * randVector, where:
    
    moveDirCoeff - coefficient for moveDir multiplication,
    gbCoeff - group best multiplier coefficient
    bestRating - rating of best solution,
    r - distance to best solution,
    x_best - position of best solution
    
"""


@dataclass
class SGD:
    # function to optimize
    optimizationFunction: object = field(default=None)
    # optimization problem
    optimizationAction: bool = field(default=True)
    # lower boundary
    lb: float = field(default=0)
    # upper boundary
    ub: float = field(default=0)
    # best solution
    __bestSolution: list = field(default_factory=list, init=False)

    # number of iterations
    iterationsNumber: int = field(default=100)
    # particles quantity
    particlesQuantity: int = field(default=30)
    # particle vision distance
    visionDistance: float = field(default=1)
    # number of points to check around
    checkPointNumber: int = field(default=8)
    # move direction coefficient
    moveDirCoeff: float = field(default=1)
    # group best coefficient multiplier
    gbCoeff: float = field(default=1)
    # random movement coefficient
    randCoeff: float = field(default=1)

    # particles array
    __particles: list = field(default_factory=list, init=False)

    def initialize(self):
        self.conditionFunc = lambda act, x, y: ((x > y) if act else (x < y))

        # 1. cycle for number of particles
        # 2. set random position
        # 3. calculate particle rating
        # 4. set rating
        # 5. initialize best result

        for i in range(self.particlesQuantity):
            pos = self.__getRandomPosition()
            p = Particle(pos)
            self.__particles.append(p)
        self.__findBestSolution()

    def run(self):
        for i in range(self.iterationsNumber):
            self.iterate()

    def iterate(self):
        self.__search()
        self.__update()

    def __search(self):

        # for each particle:
        # get point of curr pos + vision distance
        # check point around according to rotating angle
        # get point with highest rating
        # save moveDir value

        p: Particle
        for p in self.__particles:
            # get angle step (360 deg. / points number)
            deltaAngle = 2 * pi / self.checkPointNumber

            startPos = p.position + np.array([1, 0]) * self.visionDistance
            bestRating = self.__getRating(startPos)
            bestGrad = (startPos - p.position)

            # check all other points and update best moveDir
            for i in range(1, self.checkPointNumber):
                newPos = p.position + self.visionDistance * np.array([cos(i * deltaAngle), sin(i * deltaAngle)])
                newRating = self.__getRating(newPos)
                if self.conditionFunc(self.optimizationAction, newRating, bestRating):
                    bestGrad = (newPos - p.position)
                    bestRating = newRating
            p.moveDir = bestGrad

    def __update(self):

        # get best particle
        # update particles positions with rule:
        # x_new = x_old + moveDirCoeff * x_moveDir + gbCoeff * bestRating * (x_old - x_best) + randCoeff * randVector, where:
        # moveDirCoeff - coefficient for moveDir multiplication,
        # gbCoeff - group best multiplier coefficient
        # bestRating - rating of best solution,
        # r - distance to best solution,
        # x_best - position of best solution

        bestParticle = self.__findBestSolution()
        bestRating = self.__getRating(bestParticle.position)
        p: Particle
        for p in self.__particles:
            r = np.linalg.norm(p.position - bestParticle.position)
            newPos = p.position + self.moveDirCoeff * p.moveDir + self.gbCoeff * bestRating * (p.position - bestParticle.position) + self.randCoeff * np.random.uniform(
                -1, 1, 2)
            newPos = self.__boundPosition(newPos)
            p.position = newPos

    def __getRating(self, position: np.array):
        # can write other fuctions to evaluate rating R
        R = self.optimizationFunction(*position)
        return R

    def __compareRating(self, particle: Particle, partner: Particle):
        particleR = self.__getRating(particle.position)
        partnerR = self.__getRating(partner.position)
        return self.conditionFunc(self.optimizationAction, particleR, partnerR)

    def __findBestSolution(self):
        bestParticle: Particle
        bestParticle = self.__particles[0]
        bestSolution = [bestParticle.position, self.optimizationFunction(*bestParticle.position)]
        particle: Particle
        for particle in self.__particles[1:]:
            # check rating particle > rating bestParticle
            if self.__compareRating(particle, bestParticle):
                bestParticle = particle
                bestSolution[0] = bestParticle.position
                bestSolution[1] = self.optimizationFunction(*bestParticle.position)
        self.__bestSolution = bestSolution
        return bestParticle

    # random position within boundary
    def __getRandomPosition(self):
        return np.array([self.lb + random.uniform(0, 1) * (self.ub - self.lb),
                         self.lb + random.uniform(0, 1) * (self.ub - self.lb)])

    def __boundPosition(self, position: np.array):
        return np.array(
            list(map(lambda x: self.lb if x <= self.lb else (self.ub if x >= self.ub else x), position)))

    def getParticlesPositions(self):
        return [p.position for p in self.__particles]

    def getResult(self):
        return [list(map(lambda x: round(x, 3), self.__bestSolution[0])), round(self.__bestSolution[1], 3)]


def main():
    # optimizationAction: False -> min ; True -> max
    sgd = SGD(
        optimizationFunction=lambda x, y: np.cos(x / 3) * np.sin(y / 3) * np.exp(-(np.power(x / 15, 2) + np.power(y / 15, 2))),
        optimizationAction=False,
        lb=-5 * pi,
        ub=5 * pi,
        iterationsNumber=100,
        particlesQuantity=30,
        visionDistance=0.01,
        checkPointNumber=2 ** 3,
        moveDirCoeff=1.5,
        gbCoeff=0.025,
        randCoeff=0.015
    )

    sgd.initialize()

    results = []
    itersNum = 100
    for i in range(itersNum):
        res = sgd.getResult()
        results.append(res[1])
        sgd.iterate()

    fig = plt.figure(figsize=(10, 7), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_xlabel('iterations')
    ax.set_ylabel('objective function value')
    ax.plot(range(0, itersNum), results, color='blue', linestyle='-', linewidth=2)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
