from math import *
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation

from SGD import SGD


def visualize(sgd: SGD):
    x = np.linspace(sgd.lb, sgd.ub, 50)
    y = np.linspace(sgd.lb, sgd.ub, 50)
    x, y = np.meshgrid(x, y)

    z = sgd.optimizationFunction(x, y)

    fig = plt.figure(figsize=(10, 7), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim((-pi * 2, pi * 2))
    ax.view_init(45, 45)

    funcplot = ax.contour3D(x, y, z, 50, cmap=cm.get_cmap('rainbow'), alpha=0.4)
    scatFireFlies = ax.scatter([0], [0], [0], marker='o', color='black', s=20 * pi, alpha=1, edgecolors='white')
    iterText = ax.text2D(x=-0.12, y=0.1, s="iteration num")
    resPosText = ax.text2D(x=-0.12, y=0.1 - 0.01, s="reslut position")
    resValText = ax.text2D(x=-0.12, y=0.1 - 0.02, s="reslut value")

    def anim(t):
        particlesPositions = sgd.getParticlesPositions()
        scatter_x = [pos[0] for pos in particlesPositions]
        scatter_y = [pos[1] for pos in particlesPositions]
        scatter_z = [sgd.optimizationFunction(*pos) for pos in particlesPositions]

        result = sgd.getResult()

        scatFireFlies._offsets3d = (scatter_x, scatter_y, scatter_z)
        iterText.set_text(f"Itertion: {str(t)}")
        resPosText.set_text(f"coordinates: {[round(x, 3) for x in result[0]]}")
        resValText.set_text(f"value: {result[1]:.3f}")

        print(list(map(lambda x: round(x, 3), result[0])), round(result[1], 3))

        sgd.iterate()
        t += 1

        return scatFireFlies, iterText,

    anim = animation.FuncAnimation(fig=fig, func=anim, interval=1, blit=False)

    plt.interactive(False)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    pass
