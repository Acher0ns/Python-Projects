'''
Author: Kamron Cole
Originally created for assignment 13.1
Contains tests for function within palindrome module
'''
from palindrome import *

def test_string_to_palindrome():
    assert string_to_palindrome('hello') == 'hellolleh'
    assert string_to_palindrome('bad') == 'baddab'
    assert string_to_palindrome('fun') == 'funnuf'
    assert string_to_palindrome('racecar') == 'racecarracecar'
