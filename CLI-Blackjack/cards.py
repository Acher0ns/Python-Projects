'''
Author: Kamron Cole
Originally created for assignment 8.1
Various functions to create and manipulate cards
'''
import random

def make_card(rank, suit):
    '''
    Returns a tuple containing all information of a card.
    EX: Ace of Clubs
        (14, 'Clubs', 'Ace of Clubs', ' AC') // this is exluding color codes on the shortand
    '''
    # Error checking
    proper_suit = suit == 'Hearts' or suit == 'Spades' or suit == 'Clubs' or suit == 'Diamonds'
    if not proper_suit: # Makes sure a valid suit is entered
        raise ValueError('Invalid Suit: ' + str(suit))
    if rank < 2 or rank > 14: # Makes sure a valid rank is entered
        raise IndexError('Rank must be 2-14: ' + str(rank))

    red = '\033[31m'
    blue = '\033[34m'
    white = '\033[37m'
    identifier = str(rank) # Identifier used to create the name and shortand
    color = ''

    # Set identifier for face cards
    if rank == 14: identifier = 'Ace' 
    if rank == 13: identifier = 'King' 
    if rank == 12: identifier = 'Queen' 
    if rank == 11: identifier = 'Jack' 

    # Set color for cards based on suit
    if suit == 'Hearts' or suit == 'Diamonds': color = red
    if suit == 'Spades' or suit == 'Clubs': color = blue
    
    # Set the shorthand for a card
    shorthand = color + ' ' + identifier[0] + suit[0] + white
    if rank == 10: # 10 doesnt need the space
        shorthand = color + identifier + suit[0] + white

    name = identifier + ' of ' + suit
    return (rank, suit, name, shorthand)


def make_deck(shuffle_deck = False):
    '''
    Makes a deck for 52 cards
    Starts with hearts, then diamonds, then spades, then clubs
    '''
    deck = []
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    r = 2
    s = 0
    for i in range(52):
        if r > 14:
            r = 2
            s += 1
        if s > 3:
            s = 0
        deck.append(make_card(r, suits[s]))
        r += 1

    if shuffle_deck: return shuffle(deck)
    return deck


def shuffle(deck):
    '''
    Shuffles a list swaping each vlaue in the list with a random value someplace else in the list
    '''
    for index in range(0, len(deck)):
        random_index = random.randint(0, len(deck) - 1)
        swap_values_1 = deck[index]
        swap_values_2 = deck[random_index]

        deck[index] = swap_values_2
        deck[random_index] = swap_values_1
    return deck


def draw(deck):
    '''
    Draw from the back of a deck for effeciency
    '''
    return deck.pop()


def deal(deck, qty):
    '''
    Deals a number of cards from a deck to 2 hands
    '''
    if qty < 1 or qty > len(deck) / 2:
        raise IndexError('Bad qty: ' + str(qty))
    hand_1 = []
    hand_2 = []
    for i in range(qty):
        hand_1 += [draw(deck)]
        hand_2 += [draw(deck)]
    return hand_1, hand_2


def cut(deck):
    '''
    Cuts the deck into two decks that are half the length of the original
    If deck size isn't even, the first half gets an extra card
    '''
    deck_length = len(deck)
    if deck_length <= 1:
        raise ValueError('Deck must have 2 or more cards to cut it: ' + str(deck_length))

    half_length = deck_length // 2
    if deck_length % 2 == 1:
        half_length += 1

    half1 = deck[:half_length]
    half2 = deck[half_length:]

    return half1, half2


def suit_key(card: tuple) -> int:
    '''
    The sort key used to sort cards by suit then rank
    '''
    sort_key = 0

    if card[1] == 'Clubs':
        sort_key = 100
    if card[1] == 'Diamonds':
        sort_key = 200
    if card[1] == 'Hearts':
        sort_key = 300
    if card[1] == 'Spades':
        sort_key = 400

    sort_key += card[0]

    return sort_key 


def print_hand(hand: list):
    for card in hand:
        print(card[3], end = ' ')
    print()


def main():
    # Manual shuffle test
    '''
    random.seed(0)
    deck = make_deck()
    print(deck)
    shuffled = shuffle(deck)
    print(shuffled)
    '''
    # Manual sort suit key test
    deck = shuffle(make_deck())
    hand1, hand2 = deal(deck, 26)
    print('Unsorted:')
    print('  ', end = '')
    print_hand(hand1)
    print('  ', end = '')
    print_hand(hand2)
    hand1.sort(key = suit_key)
    hand2.sort(key = suit_key)
    print('Sorted:')
    print('  ', end = '')
    print_hand(hand1)
    print('  ', end = '')
    print_hand(hand2)


if __name__ == "__main__":
    main() # Runs code in main if file is ran directly (not from import)
