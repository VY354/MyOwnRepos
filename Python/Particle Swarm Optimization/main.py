from math import *
import numpy as np

from PSO_Algorithm import PSO
import Visualizing


def Solve(func, action, dx, dy, particleQuantity, inertia, personalComponent, groupComponent):
    pso = PSO()
    pso.functionToOptimize = func
    pso.action = action
    pso.deltaCoordinates = (dx, dy)
    pso.particleQuantity = particleQuantity
    pso.inertia = inertia
    pso.personalComponent = personalComponent
    pso.groupComponent = groupComponent

    pso.Initialize()

    Visualizing.vusialize(pso)


def main():
    # borders of max/min search
    dx = 10 * pi
    dy = 10 * pi

    # define function fo maximize or minimize
    func = lambda x, y: np.cos(np.square(x / 8) + np.square(y / 8))
    action = True  # True -> maximize ; False -> minimize

    particleQuantity = 30  # number of agents in algorithm
    inertia = 0.05  # velocity inertia coefficient
    personalComponent = 0.15  # personal component coefficient
    groupComponent = 1  # group componenet coefficient

    Solve(func, action, dx, dy, particleQuantity, inertia, personalComponent, groupComponent)


if __name__ == '__main__':
    main()
