from math import *
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation

from PSO_Algorithm import PSO

def vusialize(pso: PSO):
    dx = pso.deltaCoordinates[0]
    dy = pso.deltaCoordinates[1]

    x = np.linspace(-dx, dx, 50)
    y = np.linspace(-dy, dy, 50)
    x, y = np.meshgrid(x, y)

    z = pso.functionToOptimize(x, y)

    fig = plt.figure(figsize=(10, 7), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim((-3, 3))
    ax.view_init(45, 45)

    funcplot = ax.contour3D(x, y, z, 50, cmap=cm.get_cmap('binary'), alpha=0.2)
    scatParticles = ax.scatter([0], [0], [0], marker='o', color='blue', s=20 * pi, alpha=1, edgecolors='orangered')
    iterText = ax.text2D(x=-0.12, y=0.1, s="iteration num")
    resPosText = ax.text2D(x=-0.12, y=0.1 - 0.01, s="reslut position")
    resValText = ax.text2D(x=-0.12, y=0.1 - 0.02, s="reslut value")

    def anim(t):
        particlesPositions = pso.GetParticlesPositions()
        scatter_x = [pos[0] for pos in particlesPositions]
        scatter_y = [pos[1] for pos in particlesPositions]
        scatter_z = [pso.functionToOptimize(*pos) for pos in particlesPositions]

        result = pso.GetResult()

        scatParticles._offsets3d = (scatter_x, scatter_y, scatter_z)
        iterText.set_text(f"Itertion: {str(t)}")
        resPosText.set_text(f"coordinates: {[round(x, 3) for x in result[0]]}")
        resValText.set_text(f"value: {result[1]:.3f}")

        pso._Iterate()
        t += 1

        return scatParticles, iterText,

    anim = animation.FuncAnimation(fig=fig, func=anim, interval=1000, blit=False, frames=100)

    plt.interactive(False)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    vusialize()
