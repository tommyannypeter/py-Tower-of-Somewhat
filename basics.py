

class Ball:
    def __init__(self, color):
        self.color = color

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.balls = [[] * width] * height

    def initialize_balls(self):
        # fill board with balls
