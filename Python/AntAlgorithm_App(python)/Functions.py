import pygame
from dataclasses import dataclass, field, fields,asdict,astuple
from abc import ABC, abstractmethod, abstractclassmethod

from Abstracts import *
from Interfaces import *


# def DrawVertex(surface : pygame.Surface,vertex: Vertex):
#     pygame.draw.circle(
#         surface=surface,
#         center=vertex.center,
#         radius=vertex.radius,
#         width=vertex.width,
#         color=vertex.color
#     )
#
#
# def DrawLink(surface : pygame.Surface,link : Link):
#     pygame.draw.line(
#         surface=surface,
#         start_pos=link.start,
#         end_pos=link.end,
#         width=link.width,
#         color=link.color
#     )

