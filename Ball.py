# This file is for defining Ball class
# Date: 2022.06.11

from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    PURPLE = 5

class Ball:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return str(self.color.value)