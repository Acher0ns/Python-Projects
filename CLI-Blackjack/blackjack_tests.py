'''
Contains tests for blackjack.py functions
'''
import cards
import blackjack
from testing import *

def hand_score_test_1():
    '''
    makes sure hand_score is correct
    '''
    deck = cards.make_deck()
    hand1, hand2 = cards.deal(deck, 2)
    score1 = blackjack.hand_score(hand1)
    score2 = blackjack.hand_score(hand2)
    assert_equals('Hand1 Score', 21, score1, True)
    assert_equals('Hand2 Score', 20, score2, True)


def hand_score_test_2():
    '''
    makes sure hand score is correct with multiple aces
    '''
    hand1 = [(14, 'Hearts', 'Ace of Hearts', ' AH'), (10, 'Diamonds', '10 of Diamonds', '10D'), (14, 'Spades', 'Ace of Hearts', ' AS')]
    hand2 = [(10, 'Hearts', '10 of Hearts', '10H'), (14, 'Spades', 'Ace of Hearts', ' AS')]
    score1 = blackjack.hand_score(hand1)
    score2 = blackjack.hand_score(hand2)
    assert_equals('Hand1 Score', 22, score1, True)
    assert_equals('Hand2 Score', 21, score2, True)


def hand_score_test_error():
    '''
    makes sure hand_score returns and error if given an empty hand
    '''
    try:
        hand1 = []
        hand2 = []
        score1 = blackjack.hand_score(hand1)
        score2 = blackjack.hand_score(hand2)
        fail('Function should have raised an error')
    except ValueError:
        print('   Function raised a ValueError')
        pass


def dealer_hit_or_stand_test_1():
    '''
    Makes sure dealer hits if score is > 17 and > or equal to player
    '''
    player_hand = [cards.make_card(2, 'Clubs'), cards.make_card(2, 'Spades')]
    dealer_hand = [cards.make_card(2, 'Hearts'), cards.make_card(2, 'Diamonds')]
    result = blackjack.dealer_hit_or_stand(player_hand, dealer_hand)
    assert_equals('Hit', True, result, True)


def dealer_hit_or_stand_test_2():
    '''
    Makes sure dealer stands if score is > player score
    '''
    player_hand = [cards.make_card(2, 'Clubs'), cards.make_card(2, 'Spades')]
    dealer_hand = [cards.make_card(10, 'Hearts'), cards.make_card(7, 'Diamonds')]
    result = blackjack.dealer_hit_or_stand(player_hand, dealer_hand)
    assert_equals('Hit', False, result, True)


def dealer_hit_or_stand_test_3():
    '''
    makes sure to hit if player score is less than players and 17
    '''
    player_hand = [cards.make_card(13, 'Clubs'), cards.make_card(10, 'Spades')]
    dealer_hand = [cards.make_card(10, 'Hearts'), cards.make_card(7, 'Diamonds')]
    result = blackjack.dealer_hit_or_stand(player_hand, dealer_hand)
    assert_equals('Hit', True, result, True)


def dealer_hit_or_stand_test_4():
    '''
    makes sure to stand if player busts
    '''
    player_hand = [cards.make_card(11, 'Clubs'), cards.make_card(12, 'Spades'), cards.make_card(13, 'Spades')]
    dealer_hand = [cards.make_card(10, 'Hearts'), cards.make_card(6, 'Diamonds')]
    result = blackjack.dealer_hit_or_stand(player_hand, dealer_hand)
    assert_equals('Hit', False, result, True)


def run_all_tests():
    # hand_score tests
    run_test(hand_score_test_1)
    run_test(hand_score_test_2)
    run_test(hand_score_test_error)

    # dealer_hit_or_stand tests
    run_test(dealer_hit_or_stand_test_1)
    run_test(dealer_hit_or_stand_test_2)
    run_test(dealer_hit_or_stand_test_3)
    run_test(dealer_hit_or_stand_test_4)


run_all_tests()
