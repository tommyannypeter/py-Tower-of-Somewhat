# This file is for defining Board class
# Date: 2022.06.11

from Ball import Ball, Color

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.balls = self.initialize_balls()

    def initialize_balls(self):
        # fill board with balls
        balls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Ball())

            balls.append(row)
        return balls

    def __repr__(self):
        b = ""
        for row in self.balls:
            b += str(row) + "\n"
        return b
