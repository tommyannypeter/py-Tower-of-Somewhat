# This file is for defining Ball class
# Date: 2022.06.11

from Color import Color
import random

class Ball:
    def __init__(self):
        self.color = self.setColor()

    def setColor(self):
        return Color(random.randint(1, 5))

    def __repr__(self):
        return str(self.color.value)
