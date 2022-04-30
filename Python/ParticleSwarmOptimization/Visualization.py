from math import *
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation

from PSO import PSO


def visualize(pso: PSO):
    lb = pso.lb
    ub = pso.ub

    x = np.linspace(lb, ub, 50)
    y = np.linspace(lb, ub, 50)
    x, y = np.meshgrid(x, y)

    z = pso.objectiveFunction(x, y)

    fig = plt.figure(figsize=(10, 7), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim((-3, 3))
    ax.view_init(45, 45)

    funcplot = ax.contour3D(x, y, z, 50, cmap=cm.get_cmap('rainbow'), alpha=0.3)
    scatParticles = ax.scatter([0], [0], [0], marker='o', color='black', s=20 * pi, alpha=1, edgecolors='white')
    iterText = ax.text2D(x=-0.12, y=0.1, s="iteration num")
    resPosText = ax.text2D(x=-0.12, y=0.1 - 0.01, s="reslut position")
    resValText = ax.text2D(x=-0.12, y=0.1 - 0.02, s="reslut value")

    def anim(t):
        particlesPositions = pso.GetParticlesPositions()
        scatter_x = [pos[0] for pos in particlesPositions]
        scatter_y = [pos[1] for pos in particlesPositions]
        scatter_z = [pso.objectiveFunction(*pos) for pos in particlesPositions]

        result = pso.GetResult()

        scatParticles._offsets3d = (scatter_x, scatter_y, scatter_z)
        iterText.set_text(f"Itertion: {str(t)}")
        resPosText.set_text(f"coordinates: {[round(x, 3) for x in result[0]]}")
        resValText.set_text(f"value: {result[1]:.3f}")

        pso._Iterate()
        t += 1

        return scatParticles, iterText,

    anim = animation.FuncAnimation(fig=fig, func=anim, interval=250, blit=False)

    plt.interactive(False)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    pass
