'''
Author: Kamron Cole
Originally created for assignment 8.3
Contains all tests for function that cannot be tested manually
'''
import memory
import cards
from testing import *

def make_flippable_test():
    '''
    test to make sure making a card flippable doesnt change the card and flipping the card doesnt change the actual card
    '''
    card = cards.make_card(9, 'Diamonds')
    flippable = memory.make_flippable(card)
    flip_card_ele = flippable[0]
    flipped = flippable[1]

    assert_equals('Card', card, flip_card_ele, True)
    assert_equals('Flipped', False, flipped, True)
    print(' Flipping...')
    flippable[1] = True
    flipped = flippable[1]
    assert_equals('Card', card, flip_card_ele, True)
    assert_equals('Flipped', True, flipped, True)


def is_match_test_1():
    '''
    if a card is a match and face up should return true
    '''
    card1 = cards.make_card(9, 'Diamonds')
    flippable1 = memory.make_flippable(card1, True)
    card2 = cards.make_card(9, 'Diamonds')
    flippable2 = memory.make_flippable(card2, True)

    result = memory.is_match(flippable1, flippable2)
    assert_equals('Match', True, result, True)


def is_match_test_2():
    '''
    if a card isnt a match should return false
    '''
    card1 = cards.make_card(9, 'Diamonds')
    flippable1 = memory.make_flippable(card1, True)
    card2 = cards.make_card(10, 'Hearts')
    flippable2 = memory.make_flippable(card2, True)

    result = memory.is_match(flippable1, flippable2)
    assert_equals('Match', False, result, True)


def is_match_test_3():
    '''
    if cards are a match but both arent face up should return false
    '''
    card1 = cards.make_card(9, 'Diamonds')
    flippable1 = memory.make_flippable(card1, True)
    card2 = cards.make_card(9, 'Diamonds')
    flippable2 = memory.make_flippable(card2, False)

    result = memory.is_match(flippable1, flippable2)
    assert_equals('Match', False, result, True)


def is_match_test_4():
    '''
    if cards are a match and 1 is face down should return false
    '''
    card1 = cards.make_card(9, 'Diamonds')
    flippable1 = memory.make_flippable(card1, False)
    card2 = cards.make_card(9, 'Diamonds')
    flippable2 = memory.make_flippable(card2, True)

    result = memory.is_match(flippable1, flippable2)
    assert_equals('Match', False, result, True)


def is_match_test_5():
    '''
    if cards are a match but both are face down should return false
    '''
    card1 = cards.make_card(9, 'Diamonds')
    flippable1 = memory.make_flippable(card1, False)
    card2 = cards.make_card(9, 'Diamonds')
    flippable2 = memory.make_flippable(card2, False)

    result = memory.is_match(flippable1, flippable2)
    assert_equals('Match', False, result, True)


def select_cards_test_1():
    '''
    makes sure each card in selected has a matching pair
    '''
    deck = cards.make_deck()
    sel_cards = memory.select_cards(deck, 10)
    sel_cards.sort(key = cards.suit_key)

    for i in range(0, len(sel_cards), 2):
        assert_equals('Cards ' + str(i) + ' and ' + str(i + 1) + ' equality', True, sel_cards[i] == sel_cards[i + 1], True)


def select_cards_test_2():
    '''
    makes sure select_cards raises an error if an odd number is input. Can't play a matching game with and odd number of cards
    '''
    try:
        deck = cards.make_deck()
        sel_cards = memory.select_cards(deck, 9)
        fail('Function should have raised an error')
    except IndexError:
        print('   Function raised an index error')
        pass


def make_face_up_test_1():
    '''
    makes sure card gets flipped (face- up)
    '''
    board = memory.make_board(2, 2, cards.make_deck(), False)
    memory.make_face_up(1, 1, board)

    assert_equals('Card flipped up', True, board[1][1][1], True)


def make_face_up_test_2():
    '''
    makes sure a value error is raised if card is already face-up
    '''
    board = memory.make_board(2, 2, cards.make_deck(), False)
    board[1][1][1] = True
    try:
        memory.make_face_up(1, 1, board)
        fail('Function should have raised an error')
    except ValueError:
        print('   Function raised a value error')
        pass


def make_face_up_test_3():
    '''
    makes sure a value error is raised if the card trying to be flipped was already removed
    '''
    board = memory.make_board(2, 2, cards.make_deck(), False)
    memory.remove_card(1, 1, board)
    try:
        memory.make_face_up(1, 1, board)
        fail('Function should have raised an error')
    except ValueError:
        print('   Function raised a value error')
        pass


def make_face_down_test_1():
    '''
    makes sure a card gets flipped (face-down)
    '''
    board = memory.make_board(2, 2, cards.make_deck(), False)
    memory.make_face_up(1, 1, board)
    memory.make_face_down(1, 1, board)

    assert_equals('Card flipped down', False, board[1][1][1], True)


def make_face_down_test_2():
    '''
    makes sure a value error is raised if card is already face-down
    '''
    board = memory.make_board(2, 2, cards.make_deck(), False)
    board[1][1][1] = False
    try:
        memory.make_face_down(1, 1, board)
        fail('Function should have raised an error')
    except ValueError:
        print('   Function raised a value error')
        pass


def make_face_down_test_3():
    '''
    makes sure a value error is raised if the card trying to be flipped was already removed
    '''
    board = memory.make_board(2, 2, cards.make_deck(), False)
    memory.remove_card(1, 1, board)
    try:
        memory.make_face_down(1, 1, board)
        fail('Function should have raised an error')
    except ValueError:
        print('   Function raised a value error')
        pass


def run_all_tests():
    '''
    contains all tests for memory.py functions
    '''

    # make_flippable tests
    run_test(make_flippable_test)

    # is_match tests
    run_test(is_match_test_1)
    run_test(is_match_test_2)
    run_test(is_match_test_3)
    run_test(is_match_test_4)
    run_test(is_match_test_5)

    # select_cards tests
    run_test(select_cards_test_1)
    run_test(select_cards_test_2)

    # make_face_up tests 
    run_test(make_face_up_test_1)
    run_test(make_face_up_test_2)
    run_test(make_face_up_test_3)

    # make_face_down tests
    run_test(make_face_down_test_1)
    run_test(make_face_down_test_2)
    run_test(make_face_down_test_3)


run_all_tests() # runs code in run_all_tests
