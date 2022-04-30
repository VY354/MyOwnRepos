from math import *
import numpy as np

from PSO import PSO
import Visualization


def Solve(objectiveFunction, optimizationAction, lb, ub, particleQuantity, inertiaComponent, personalComponent,
          groupComponent):
    pso = PSO()
    pso.objectiveFunction = objectiveFunction
    pso.optimizationAction = optimizationAction
    pso.lb = lb
    pso.ub = ub
    pso.particleQuantity = particleQuantity
    pso.inertiaComponent = inertiaComponent
    pso.personalComponent = personalComponent
    pso.groupComponent = groupComponent

    pso.Initialize()
    Visualization.visualize(pso)


def main():
    # borders of max/min search
    lb = -2 * pi
    ub = 2 * pi

    # define function fo maximize or minimize
    objectiveFunction = lambda x, y: np.cos(x / 2) * np.sin(y / 2)
    optimizationAction = False  # True -> maximize ; False -> minimize

    particleQuantity = 30  # number of agents in algorithm
    inertiaComponent = 0.05  # velocity inertiaComponent coefficient
    personalComponent = 0.2  # personal component coefficient
    groupComponent = 1  # group component coefficient

    Solve(objectiveFunction, optimizationAction, lb, ub, particleQuantity, inertiaComponent, personalComponent,
          groupComponent)


if __name__ == '__main__':
    main()
