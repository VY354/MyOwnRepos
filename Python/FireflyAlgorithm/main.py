from math import *
import numpy as np

from FA import FA
import Visualization


def main():
    fa = FA(
        optimizationFunction=lambda x, y: np.cos(x / 2 + 0.5) * np.sin(y / 2 + 0.5),
        optimizationAction=False,
        lb=-2 * pi,
        ub=2 * pi,
        iterationsNumber=100,
        firefliesQuantity=30,
        gamma=0.15,
        alpha=0.45)

    fa.initialize()
    Visualization.visualize(fa)


if __name__ == '__main__':
    main()
