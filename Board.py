# This file is for defining Board class
# Date: 2022.06.11

from Ball import Ball, Color
import random

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.balls = []
        self.initialize_balls()

    def initialize_balls(self):
        # fill board with balls
        for i in range (self.height):
            row = []
            for j in range(self.width):
                row.append(Ball(Color(random.randint(1, 5))))

            self.balls.append(row)

    def __repr__(self):
        for row in self.balls:
            print(row)
        return ""