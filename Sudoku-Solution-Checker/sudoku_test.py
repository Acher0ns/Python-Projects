from sudoku import *

DATA_PATH = 'data/'

def test_file_to_list():
    actual = file_to_list(DATA_PATH + 'valid_001.sud')
    expected = [[8, 9, 2, 5, 7, 3, 4, 1, 6], [6, 4, 7, 1, 8, 9, 3, 5, 2], [1, 5, 3, 2, 6, 4, 8, 9, 7], [2, 3, 5, 6, 4, 7, 1, 8, 9], [9, 1, 4, 8, 2, 5, 7, 6, 3], [7, 6, 8, 3, 9, 1, 5, 2, 4], [3, 2, 6, 7, 1, 8, 9, 4, 5], [4, 7, 1, 9, 5, 6, 2, 3, 8], [5, 8, 9, 4, 3, 2, 6, 7, 1]]
    assert actual == expected


def test_file_to_list_invalid_file():
    actual = file_to_list(DATA_PATH + '/invalid_filename')
    expected = None
    assert actual == expected


def test_sudoku_valid():
    valid_board = file_to_list(DATA_PATH + 'valid_001.sud')
    actual = valid_solution(valid_board)
    expected = True
    assert actual == expected

def test_sudoku_invalid():
    invalid_board = file_to_list(DATA_PATH + 'invalid_001.sud')
    actual = valid_solution(invalid_board)
    expected = False
    assert actual == expected