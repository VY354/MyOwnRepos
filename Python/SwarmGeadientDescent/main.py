from math import *
import numpy as np

from SGD import SGD
import Visualization


def main():
    sgd = SGD(
        optimizationFunction=lambda x, y: np.cos(x / 2) * np.sin(y / 2),
        optimizationAction=False,
        lb=-2 * pi,
        ub=2 * pi,
        iterationsNumber=100,
        particlesQuantity=30,
        visionDistance=0.01,
        checkPointNumber=8,
        absorption=1,
        gradCoeff=0.05,
        randCoeff=0.01
    )

    sgd.initialize()
    Visualization.visualize(sgd)


if __name__ == '__main__':
    main()
