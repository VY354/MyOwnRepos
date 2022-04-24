from math import *

import random

import numpy as np

from numba import jit, njit, int32, float32,float64,f8
from numba.experimental import jitclass

from perlin_noise import perlin_noise

import PIL
from PIL import Image, ImageDraw, ImageColor

import time

import pygame

from dataclasses import dataclass
from enum import Enum

#=========================================================



WIDTH, HEIGHT = 800,600
WIN_FILL_COLOR  = (0,0,0)
FPS = 60

pygame.init()


WIN = pygame.display.set_mode((WIDTH,HEIGHT),pygame.SCALED)
Surface_Links = pygame.Surface((WIDTH,HEIGHT))
pygame.display.set_caption('My first window caption!')

fontObj1=pygame.font.SysFont('arial',30)

#=========================================================



