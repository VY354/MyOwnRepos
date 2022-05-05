import random
import numpy as np
from dataclasses import dataclass, field, fields, asdict, astuple


@dataclass
class Particle:
    position: np.array = field(default_factory=np.array)
    gradient: np.array = field(default=np.array([0,0]),init=False)


def main():
    particle = Particle(np.array([0, 0]))
    print(asdict(particle))


if __name__ == '__main__':
    main()
