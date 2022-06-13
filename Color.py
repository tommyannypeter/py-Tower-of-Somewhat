from enum import Enum
import random

class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)

    def get_random_color():
        return random.choice([Color.RED, Color.GREEN, Color.BLACK, Color.YELLOW, Color.PURPLE])
