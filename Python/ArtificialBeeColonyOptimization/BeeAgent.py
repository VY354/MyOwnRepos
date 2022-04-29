import numpy as np
from dataclasses import dataclass, field, fields, asdict, astuple

@dataclass
class Bee:
    # position
    position: np.array = field(default=np.array, init=False)
    # trial
    trial: int = field(default=0,init=False)

def main():
    b = Bee()
    b.position = np.random.rand(2)

    print(asdict(b))

if __name__ == '__main__':
    main()
