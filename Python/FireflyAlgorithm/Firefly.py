import random
import numpy as np
from dataclasses import dataclass, field, fields, asdict, astuple


@dataclass
class Firefly:
    position: np.array = field(default_factory=np.array, init=True)
    defaultAttractiveness: float = field(default=1, init=True)


def main():
    firefly = Firefly(np.random.random(3), random.uniform(-100, 100))
    print(asdict(firefly))


if __name__ == '__main__':
    main()
