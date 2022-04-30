import random
from math import *

import numpy as np
from dataclasses import dataclass, field, fields, asdict, astuple

from BeeAgent import Bee


@dataclass
class ABC:
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

    # max iteration
    maxIteration: int = field(default=0, init=True)
    # number of bees
    beesQuantity: int = field(default=0, init=True)
    # max trial value
    maxTrialValue: int = field(default=0, init=True)

    # bees array
    __bees: list = field(default_factory=list, init=False)

    # initialize bees
    def initialize(self):
        self.conditionFunc = lambda act, x, y: ((x > y) if act else (x < y))
        b: Bee
        for i in range(self.beesQuantity):
            x = self.lb + random.uniform(0, 1) * (self.ub - self.lb)
            y = self.lb + random.uniform(0, 1) * (self.ub - self.lb)
            b = Bee()
            b.position = np.array([x, y])
            self.__bees.append(b)
        self.__bestSolution = [self.__bees[0].position, self.optimizationFunction(*self.__bees[0].position)]

    # run
    def run(self):
        for i in range(self.maxIteration):
            self.iterate()

    def iterate(self):
        self.__employeePhase()
        self.__onlookerPhase()
        self.__memorizeBestSolution()
        # print(list(map(lambda x: round(x, 3), self.__bestSolution[0])), round(self.__bestSolution[1], 3))
        self.__scoutPhase()

    # emoloyees bee phase
    def __employeePhase(self):
        b: Bee
        for b in self.__bees:
            newPos = self.generateNewSolution(b)
            self.updateBee(b, newPos)

    # onlooker bee phase
    def __onlookerPhase(self):
        # start chosen food sources tracker counter
        # start curr. bee index tracker

        # generate food sources probabilities list

        # while food sources tracker > 0:
        # for curr. bee generate rand(0,1)
        # if rand <= curr food source prob.:
        # set this food source pos. to curr. bee pos.
        # food tracker ++
        # pop this food source from lost
        # go to next bee
        # else:
        # go to next food source

        solutionIndex = 0
        beeIndex = 0

        fitSum = np.sum([self.__fitness(b.position) for b in self.__bees], axis=0)
        solutionProbList = np.array([self.__fitness(b.position) / fitSum for b in self.__bees])
        maxProb = np.max(solutionProbList)

        while beeIndex < len(self.__bees):
            if solutionIndex >= np.shape(solutionProbList)[0]:
                solutionIndex = 0
            rndNum = random.uniform(0, maxProb)
            if rndNum <= solutionProbList[solutionIndex]:
                b: Bee
                b = self.__bees[beeIndex]
                b.position = self.__bees[solutionIndex].position
                newPos = self.generateNewSolution(b)

                self.updateBee(b, newPos)

                beeIndex += 1

            solutionIndex += 1

    # scout bee phase
    def __scoutPhase(self):
        # get list of bees, which trial > limit
        # randomly choose bee and set random position

        stuckedBees = [b for b in self.__bees if b.trial > self.maxTrialValue]
        if stuckedBees:
            b: Bee
            b = random.choice(stuckedBees)
            b.position = np.array([self.lb + random.uniform(0, 1) * (self.ub - self.lb),
                                   self.lb + random.uniform(0, 1) * (self.ub - self.lb)])
            b.trial = 0

    # generate new solution
    def generateNewSolution(self, b: Bee):
        # for each bee:
        # randomly take other bee
        # change coordinate according to  formula

        partner: Bee
        partner = random.choice([bb for bb in self.__bees if bb is not b])

        # upd rule: X_i_new = X_i + rand(0,1)*(X_i - X_k), where
        # i - current bee
        # k - other bee
        newPos = b.position + random.uniform(-1, 1) * (np.array(b.position) - np.array(partner.position))
        newPos = list(map(lambda x: self.lb if x <= self.lb else (self.ub if x >= self.ub else x), newPos))

        return newPos

    # calculate fitness
    def __fitness(self, pos: np.array):
        funcValue = self.optimizationFunction(*pos)
        if self.optimizationAction == True:
            return exp(funcValue)
        elif self.optimizationAction == False:
            return 1.0 / (1.0 + funcValue) if funcValue >= 0 else 1.0 + abs(funcValue)

    def updateBee(self, b: Bee, newPos: np.array):
        currFitness = self.__fitness(b.position)
        newFitness = self.__fitness(newPos)

        if newFitness > currFitness:
            b.position = newPos
            b.trial = 0
        else:
            b.trial += 1

    # save best result
    def __memorizeBestSolution(self):
        for b in self.__bees:
            if self.__fitness(b.position) > self.__fitness(self.__bestSolution[0]):
                self.__bestSolution = [b.position, self.optimizationFunction(*b.position)]

    # get result
    def getResult(self):
        return self.__bestSolution

    def getBeesPosotions(self):
        return [b.position for b in self.__bees]

    pass


def main():
    abc = ABC(
        optimizationFunction=(lambda x, y: np.cos(np.square(x) + np.square(y))),
        optimizationAction=False,
        lb=-2 * pi,
        ub=2 * pi,
        maxIteration=100,
        beesQuantity=30,
        maxTrialValue=5
    )

    abc.initialize()
    abc.run()

    res = abc.getResult()
    print(list(map(lambda x: round(x, 3), res[0])), round(res[1], 3))


if __name__ == '__main__':
    main()
