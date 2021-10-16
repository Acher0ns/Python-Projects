'''
Author: Kamron Cole
Originally created for assignment 8.1
Contains all tests for functions in card.py
'''
import cards
import random
from testing import *

# Colors use in shorthand
red = '\033[31m'
blue = '\033[34m'
white = '\033[37m'

def make_card_2_test():
    '''
    Makes 2 of hearts
    makes sure correct card is returned
    '''
    result = cards.make_card(2, 'Hearts')
    assert_equals('Rank', 2, result[0], True)
    assert_equals('Suit', 'Hearts', result[1], True)
    assert_equals('Name', '2 of Hearts', result[2], True)
    assert_equals('Shorthand', red + ' 2H' + white, result[3], True)


def make_card_10_test():
    '''
    Makes 10 of spades
    makes sure correct card is returned
    '''
    result = cards.make_card(10, 'Spades')
    assert_equals('Rank', 10, result[0], True)
    assert_equals('Suit', 'Spades', result[1], True)
    assert_equals('Name', '10 of Spades', result[2], True)
    assert_equals('Shorthand', blue + '10S' + white, result[3], True)


def make_jack_test():
    '''
    Makes Jack of diamonds
    makes sure correct card is returned
    '''
    result = cards.make_card(11, 'Diamonds')
    assert_equals('Rank', 11, result[0], True)
    assert_equals('Suit', 'Diamonds', result[1], True)
    assert_equals('Name', 'Jack of Diamonds', result[2], True)
    assert_equals('Shorthand', red + ' JD' + white, result[3], True)


def make_queen_test():
    '''
    Makes Queen of clubs
    makes sure correct card is returned
    '''
    result = cards.make_card(12, 'Clubs')
    assert_equals('Rank', 12, result[0], True)
    assert_equals('Suit', 'Clubs', result[1], True)
    assert_equals('Name', 'Queen of Clubs', result[2], True)
    assert_equals('Shorthand', blue + ' QC' + white, result[3], True)


def make_king_test():
    '''
    Makes King of hearts
    makes sure correct card is returned
    '''
    result = cards.make_card(13, 'Hearts')
    assert_equals('Rank', 13, result[0], True)
    assert_equals('Suit', 'Hearts', result[1], True)
    assert_equals('Name', 'King of Hearts', result[2], True)
    assert_equals('Shorthand', red + ' KH' + white, result[3], True)


def make_ace_test():
    '''
    Makes Ace of spades
    makes sure correct card is returned
    '''
    result = cards.make_card(14, 'Spades')
    assert_equals('Rank', 14, result[0], True)
    assert_equals('Suit', 'Spades', result[1], True)
    assert_equals('Name', 'Ace of Spades', result[2], True)
    assert_equals('Shorthand', blue + ' AS' + white, result[3], True)


def make_card_test_error_1():
    '''
    Makes sure error is raised if an inproper suit is entered
    '''
    try:
        result = cards.make_card(14, 'Crabs')
        fail('Function should have raised an error')
    except ValueError:
        print('   Function raised a ValueError')
        pass


def make_card_test_error_2():
    '''
    Makes sure an error is raised when a rank less than 2 is entered
    '''
    try:
        result = cards.make_card(1, 'Clubs')
        fail('Function should have raised an error')
    except IndexError:
        print('   Function raised an IndexError')
        pass


def make_card_test_error_3():
    '''
    Makes sure an error is raised when a rank greater than 14 is entered
    '''
    try:
        result = cards.make_card(15, 'Clubs')
        fail('Function should have raised an error')
    except IndexError:
        print('   Function raised an IndexError')
        pass


def make_deck_test():
    '''
    Tests various card to make sure their posiition and card is right
    '''
    result = cards.make_deck()
    assert_equals('Card 0', (2, 'Hearts', '2 of Hearts', red + ' 2H' + white), result[0], True)
    assert_equals('Card 13', (2, 'Diamonds', '2 of Diamonds', red + ' 2D' + white), result[13], True)
    assert_equals('Card 26', (2, 'Spades', '2 of Spades', blue + ' 2S' + white), result[26], True)
    assert_equals('Card 39', (2, 'Clubs', '2 of Clubs', blue + ' 2C' + white), result[39], True)
    assert_equals('Card 51', (14, 'Clubs', 'Ace of Clubs', blue + ' AC' + white), result[51], True)


def make_deck_test_shuffle():
    '''
    Makes sure shuffle shuffles the deck
    '''
    random.seed(0)
    deck = cards.make_deck()
    shuffled_deck = cards.make_deck(shuffle_deck = True)

    card_changed = shuffled_deck[1] != deck[1]
    assert_equals('Card 1 changed', True, card_changed, True)
    card_changed = shuffled_deck[2] != deck[2]
    assert_equals('Card 2 changed', True, card_changed, True)
    card_changed = shuffled_deck[3] != deck[3]
    assert_equals('Card 3 changed', True, card_changed, True)
    card_changed = shuffled_deck[4] != deck[4]
    assert_equals('Card 4 changed', True, card_changed, True)
    card_changed = shuffled_deck[5] != deck[5]
    assert_equals('Card 5 changed', True, card_changed, True)
    card_changed = shuffled_deck[6] != deck[6]
    assert_equals('Card 6 changed', True, card_changed, True)


def shuffle_test():
    '''
    Makes sure shuffle shuffles the deck
    '''
    random.seed(0)
    deck = cards.make_deck()
    copy_deck = cards.make_deck()
    shuffled_deck = cards.shuffle(copy_deck)

    card_changed = shuffled_deck[1] != deck[1]
    assert_equals('Card 1 changed', True, card_changed, True)
    card_changed = shuffled_deck[2] != deck[2]
    assert_equals('Card 2 changed', True, card_changed, True)
    card_changed = shuffled_deck[3] != deck[3]
    assert_equals('Card 3 changed', True, card_changed, True)
    card_changed = shuffled_deck[4] != deck[4]
    assert_equals('Card 4 changed', True, card_changed, True)
    card_changed = shuffled_deck[5] != deck[5]
    assert_equals('Card 5 changed', True, card_changed, True)
    card_changed = shuffled_deck[6] != deck[6]
    assert_equals('Card 6 changed', True, card_changed, True)


def draw_test():
    '''
    makes sure draw draws from the back of a deck and removes the drawn card from the deck
    '''
    deck = cards.make_deck()
    last_card = deck[len(deck) - 1]
    drew_card = cards.draw(deck)

    assert_equals('Deck length', 51, len(deck), True)
    assert_equals('Drawn Card', last_card, drew_card, True)


def deal_test():
    '''
    make sure both hands are of appropriate length after dealing
    '''
    hand1, hand2 = cards.deal(cards.make_deck(), 5)
    assert_equals('Hand 1 size', 5, len(hand1), True)
    assert_equals('Hand 2 size', 5, len(hand2), True)


def deal_test_error_1():
    '''
    make sure deal raises an error if qty is 0
    '''
    try:
        hand1, hand2 = cards.deal(cards.make_deck(), 0)
        fail('Function should have raised an error')
    except IndexError:
        print('   Function raised a value error')
        pass


def deal_test_error_2():
    '''
    make sure deal raises an error if qty is over deck size
    '''
    try:
        hand1, hand2 = cards.deal(cards.make_deck(), 53)
        fail('Function should have raised an error')
    except IndexError:
        print('   Function raised a value error')
        pass


def cut_test_even():
    '''
    Tests the length of both halves when the deck has an even number of cards and is cut
    '''
    deck = cards.make_deck()
    half1, half2 = cards.cut(deck)
    assert_equals('Length of half 1', 26, len(half1), True)
    assert_equals('Length of half 2', 26, len(half2), True)


def cut_test_odd():
    '''
    Tests the length of both halves when the deck has an odd number of cards and is cut
    '''
    deck = cards.make_deck()
    cards.draw(deck)
    half1, half2 = cards.cut(deck)
    assert_equals('Length of half 1', 26, len(half1), True)
    assert_equals('Length of half 2', 25, len(half2), True)


def cut_test_error_1():
    '''
    Makes sure cut raises an error when the deck length is 0
    '''
    try:
        deck = []
        result = cards.cut(deck)
        fail('Function should have raised an error.')
    except ValueError:
        print('   Function raised a ValueError')
        pass


def cut_test_error_2():
    '''
    Makes sure cut raises an error when the deck length is 1
    '''
    try:
        hand1, hand2 = cards.deal(cards.make_deck(), 1)
        result = cards.cut(hand1)
        fail('Function should have raised an error.')
    except ValueError:
        print('   Function raised a ValueError')
        pass


def run_all_tests():
    '''
    Runs all tests...
    '''
    # make_card tests
    run_test(make_card_2_test)
    run_test(make_card_10_test)
    run_test(make_jack_test)
    run_test(make_queen_test)
    run_test(make_king_test)
    run_test(make_ace_test)
    run_test(make_card_test_error_1)
    run_test(make_card_test_error_2)
    run_test(make_card_test_error_3)

    # make_deck tests
    run_test(make_deck_test)
    run_test(make_deck_test_shuffle)

    # shuffle tests
    run_test(shuffle_test)

    # draw tests
    run_test(draw_test)

    # deal tests
    run_test(deal_test)
    run_test(deal_test_error_1)
    run_test(deal_test_error_2)

    # cut tests
    run_test(cut_test_even)
    run_test(cut_test_odd)
    run_test(cut_test_error_1)
    run_test(cut_test_error_2)


run_all_tests()
