import io
from tic_tac_toe import *

def convert_to_board(board: str) -> list:
    '''
    Converts the board output string to a list
    '''
    answer = []
    rows = board.split('\n')
    for i in range(0, len(rows), 2):
        answer.append(rows[i].split('|'))
    return answer


def test_make_board():
    expected = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    actaul = make_board()
    assert str(actaul) == str(expected)


def test_print_board(capsys):
    expected = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board(make_board())
    captured_out = capsys.readouterr().out
    actual = convert_to_board(captured_out)
    assert expected == actual

def test_make_move(monkeypatch, capsys):
    board = [['X', ' ', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    expected = [['X', 'X', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    symbol = 'X'
    location = io.StringIO('0 1\n')
    monkeypatch.setattr('sys.stdin', location)
    make_move(board, symbol)
    captured_out = capsys.readouterr().out[22:] # capsys was capturing the prompt text as well, slicing removes it from the string
    actual = convert_to_board(captured_out)
    assert actual == expected


def test_make_move_used(monkeypatch, capsys):
    board = [['X', ' ', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    expected_out = 'Invalid move. Please try again.'
    symbol = 'X'
    monkeypatch.setattr('sys.stdin', io.StringIO('0 0\n0 1\n')) # two moves because of the while loop in make moves will freeze the test
    make_move(board, symbol)
    actual = capsys.readouterr().out[22:53] # capsys was capturing the prompt text as well, slicing removes it from the string
    assert actual == expected_out


def test_make_move_invalid(monkeypatch, capsys):
    board = [['X', ' ', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    expected_out = 'Invalid move. Please try again.'
    symbol = 'X'
    monkeypatch.setattr('sys.stdin', io.StringIO('o 0\n0 1\n')) # two moves because of the while loop in make moves will freeze the test
    make_move(board, symbol)
    actual = capsys.readouterr().out[22:53] # capsys was capturing the prompt text as well, slicing removes it from the string
    assert actual == expected_out


def test_main(monkeypatch, capsys):
    expected = 'Game over!'
    monkeypatch.setattr('sys.stdin', io.StringIO('0 0\n0 1\n0 2\n1 0\n 1 1\n 1 2\n2 0\n 2 1\n 2 2\n')) # two moves because of the while loop in make moves will freeze the test
    main()
    actual = capsys.readouterr().out.strip().split('\n')
    assert expected == actual[-1]
