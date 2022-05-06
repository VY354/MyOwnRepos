from math import *
import numpy as np

from SGD import SGD
import Visualization


def main():
    sgd = SGD(
        optimizationFunction=lambda x, y: np.cos(x / 3) * np.sin(y / 3) * np.exp(-(np.power(x / 15, 2) + np.power(y / 15, 2))),
        optimizationAction=False,
        lb=-5 * pi,
        ub=5 * pi,
        iterationsNumber=100,
        particlesQuantity=30,
        visionDistance=0.01,
        checkPointNumber=2 ** 3,
        absorption=0.25,
        moveDirCoeff=1.5,
        gbCoeff=0.025,
        randCoeff=0.015
    )

    sgd.initialize()
    Visualization.visualize(sgd)


if __name__ == '__main__':
    main()
