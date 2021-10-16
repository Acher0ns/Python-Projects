'''
Author: Kamron Cole
Contains test for hash_race.py functions
'''
import random
from hash_race import *

def test_very_bad_hash():
    '''
    Tests that the same hash is returned by very_bad_hash using various strings.
    '''
    string_1 = 'Hi'
    string_2 = 'Hello'
    string_3 = 'No'
    string_4 = 'Yes'
    string_5 = 'Blue'
    string_6 = 'Green'
    hash_1 = very_bad_hash(string_1)
    hash_2 = very_bad_hash(string_2)
    hash_3 = very_bad_hash(string_3)
    hash_4 = very_bad_hash(string_4)
    hash_5 = very_bad_hash(string_5)
    hash_6 = very_bad_hash(string_6)
    assert hash_1 == 0
    assert hash_2 == 0
    assert hash_3 == 0
    assert hash_4 == 0
    assert hash_5 == 0
    assert hash_6 == 0


def test_inconsistent_hash():
    '''
    Tests that the inconsistant_hash function may return different hashes for the same function
    '''
    try:
        random.seed(0)
        string = 'Same'
        hash_1 = inconsistent_hash(string)
        hash_2 = inconsistent_hash(string)
        hash_3 = inconsistent_hash(string)
        hash_4 = inconsistent_hash(string)
        hash_5 = inconsistent_hash(string)
        hash_6 = inconsistent_hash(string)
        assert type(hash_1) == int
        assert hash_1 == hash_2
        assert hash_1 == hash_3
        assert hash_1 == hash_4
        assert hash_1 == hash_5
        assert hash_1 == hash_6
        int('ok') # Forces test to fail if all hashes are equal meaning hash function is relatively consistent
    except AssertionError:
        pass


def test_sum_ascii_hash():
    '''
    test that sum_ascii_hash properly returns the sum of the ascii codes of characters in a string
    '''
    string = '  '
    expected = 64
    actual = sum_ascii_hash(string)
    assert actual == expected


def test_better_hash():
    '''
    Tests that better_hash returns the expected values given 2 strings
    '''
    string_1 = 'abcd'
    string_2 = 'bdca'
    expected_1 = 2987074
    expected_2 = 3018784
    actual_1 = better_hash(string_1)
    actual_2 = better_hash(string_2)
    assert actual_1 == expected_1 and actual_2 == expected_2


def test_count_collisions(capsys):
    '''
    Test for count_collisions function based on the expected output given in the assignment pdf
    '''
    expected = '  total collisions: 17575\n  average collisions: 17575.0'
    count_collisions(very_bad_hash, 100000)
    output = capsys.readouterr().out
    assert expected in output
