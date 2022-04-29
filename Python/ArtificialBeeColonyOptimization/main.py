from math import *
import numpy as np

from ABC import ABC
from Visualization import visualize


def main():

    abc = ABC(
        optimizationFunction=(lambda x, y: np.cos(x / 2) * np.sin(y / 2)),
        optimizationAction=True,
        lb=-2 * pi,
        ub=2 * pi,
        maxIteration=100,
        beesQuantity=30,
        maxTrialValue=20
    )

    abc.initialize()

    abc.run()
    res = abc.getResult()
    print(list(map(lambda x: round(x, 3), res[0])), round(res[1], 3))

    visualize(abc)


if __name__ == '__main__':
    main()
