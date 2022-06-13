# This file is for simple testing the Board and Ball class
# Date: 2022.06.11

from Board import Board

if __name__ == "__main__":
    board = Board(5, 6)
    print(board)

    assert len(board.balls) == 5
    assert len(board.balls[0]) == 6
