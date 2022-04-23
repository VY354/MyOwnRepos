
import numpy as np

import dataclasses
from dataclasses import dataclass,field,fields, asdict,astuple

@dataclass
class Particle:
    position: np.array = field(default=None,init=False)
    velocity: float = field(default=0,init=False)
    personalBestPosition: np.array =field(default=None,init=False)
    personalBestValue: float = field(default=0,init=False)
