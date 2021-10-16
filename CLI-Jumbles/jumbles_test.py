import io
from jumbles import *

DATA_PATH = 'data/'

def test_dictionary_len():
    expected = 5
    actual = len(dictionary(DATA_PATH + 'words_small.txt'))
    assert actual == expected


def test_dictionary_lower():
    for word in dictionary(DATA_PATH + 'words_small.txt'):
        assert word == word.lower()


def test_letters_in_word_normal():
    expected = 'aaccerr'
    actual = letters_in_word('racecar')
    assert actual == expected


def test_jambles():
    words = dictionary(DATA_PATH + 'words_small.txt')
    expected = {'aet': ['ate', 'eat', 'tea'], 'loot': ['loot', 'tool']}
    actual = jambles(words)
    assert actual == expected


def test_find_solution_in_dict_single():
    words = dictionary(DATA_PATH + 'words.txt')
    solutions = jambles(words)

    expected = 'auburn'
    actual = find_solution_in_dict('UNBRAU', solutions)
    assert actual == expected


def test_find_solution_in_dict_multi(monkeypatch):
    words = dictionary(DATA_PATH + 'words.txt')
    solutions = jambles(words)

    expected = 'prize'
    monkeypatch.setattr('sys.stdin', io.StringIO('1'))
    actual = find_solution_in_dict('ZIPER', solutions)
    assert actual == expected


def test_find_solution_in_dict_IndexError(monkeypatch):
    words = dictionary(DATA_PATH + 'words.txt')
    solutions = jambles(words)

    expected = 'prize'
    monkeypatch.setattr('sys.stdin', io.StringIO('10\n1'))
    actual = find_solution_in_dict('ZIPER', solutions)
    assert actual == expected


def test_find_solution_in_dict_ValueError(monkeypatch):
    words = dictionary(DATA_PATH + 'words.txt')
    solutions = jambles(words)

    expected = 'pierz'
    monkeypatch.setattr('sys.stdin', io.StringIO('a\n0'))
    actual = find_solution_in_dict('ZIPER', solutions)
    assert actual == expected


def test_find_solution_in_dict_KeyError(capsys):
    words = dictionary(DATA_PATH + 'words.txt')
    solutions = jambles(words)

    expected = '"0102938" has no possible solutions.\n'
    find_solution_in_dict('0102938', solutions)
    actual = capsys.readouterr().out
    assert actual == expected


def test_prompt_for_clue(monkeypatch):
    words = dictionary(DATA_PATH + 'words.txt')
    solutions = jambles(words)

    expected_word = 'thrash'
    expected_letters = 'hs'
    monkeypatch.setattr('sys.stdin', io.StringIO('SHARTH 1 4'))
    actual_word, actual_letters = prompt_for_clue()
    assert actual_word == expected_word
    assert actual_letters == expected_letters


def test_prompt_for_clue_IndexError(monkeypatch):
    words = dictionary(DATA_PATH + 'words.txt')
    solutions = jambles(words)

    expected_word = 'thrash'
    expected_letters = 'hs'
    monkeypatch.setattr('sys.stdin', io.StringIO('SHARTH 1 10\nSHARTH 1 4'))
    actual_word, actual_letters = prompt_for_clue()
    assert actual_word == expected_word
    assert actual_letters == expected_letters


def test_prompt_for_clue_ValueError(monkeypatch):
    words = dictionary(DATA_PATH + 'words.txt')
    solutions = jambles(words)

    expected_word = 'thrash'
    expected_letters = 'hs'
    monkeypatch.setattr('sys.stdin', io.StringIO('SHARTH a b\nSHARTH 1 4'))
    actual_word, actual_letters = prompt_for_clue()
    assert actual_word == expected_word
    assert actual_letters == expected_letters


def test_main(monkeypatch, capsys):
    expected = GREEN + 'solution: rubbish' + WHITE + '\n'
    clue1 = 'klayb 0\n0'
    clue2 = 'ziper 1 2\n1'
    clue3 = 'unbrau 1 2'
    clue4 = 'sharth 1 4'
    clues = clue1 + '\n' + clue2 + '\n' + clue3 + '\n' + clue4
    monkeypatch.setattr('sys.stdin', io.StringIO(clues))
    main()
    actual = capsys.readouterr().out
    assert expected in actual
