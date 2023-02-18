from board import Board

def test_board():
    board = Board(5, 6)
    print(board)

    assert len(board.balls) == 5
    assert len(board.balls[0]) == 6
