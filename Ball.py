# This file is for defining Ball class
# Date: 2022.06.11

from Color import Color
import random

class Ball:
    def __init__(self):
        self.color = self.setColor()

    def setColor(self):
        color = Color
        return color.get_random_color()

    def __repr__(self):
        return str(self.color.name)
