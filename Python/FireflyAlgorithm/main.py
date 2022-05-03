from math import *
import numpy as np

from FA import FA
import Visualization


def main():
    fa = FA(
        optimizationFunction=lambda x, y: np.cos(x / 2) * np.sin(y / 2),
        optimizationAction=False,
        lb=-2 * pi,
        ub=2 * pi,
        iterationsNumber=100,
        firefliesQuantity=30,
        gamma=20,
        alpha=0.5)

    fa.initialize()
    # fa.run()
    # print(fa.getResult())

    Visualization.visualize(fa)


if __name__ == '__main__':
    main()
