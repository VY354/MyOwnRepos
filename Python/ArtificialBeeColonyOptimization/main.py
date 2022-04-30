from math import *
import numpy as np

from ABC import ABC
from Visualization import visualize


def main():
    abc = ABC(
        optimizationFunction=(lambda x, y: np.cos(x / 1.5) * np.sin(y / 1.5)),
        optimizationAction=False,
        lb=-2 * pi,
        ub= 2 * pi,
        maxIteration=100,
        beesQuantity=30,
        maxTrialValue=5
    )

    abc.initialize()
    visualize(abc)


if __name__ == '__main__':
    main()
