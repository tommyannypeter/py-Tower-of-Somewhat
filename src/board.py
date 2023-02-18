# This file is for defining Board class
# Date: 2022.06.11

from ball import Ball

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.balls = self.initialize_balls()

    def __repr__(self):
        ball_name = ""
        for row in self.balls:
            ball_name += str(row) + "\n"
        return ball_name

    def initialize_balls(self):
        # fill board with balls
        balls = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(Ball())

            balls.append(row)
        return balls
