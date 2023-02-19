# This file is for defining Ball class
# Date: 2022.06.11

import random
from color import Color

class Ball:
    def __init__(self):
        self.color = random.choice([Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.PURPLE])

    def __repr__(self):
        return str(self.color.name)
