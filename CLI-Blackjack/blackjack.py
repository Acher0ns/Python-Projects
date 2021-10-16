'''
Auhtor: Kamron Cole
Originally created for assignment 8.2
'''
import cards

def hand_score(hand: list) -> int:
    '''
    Returns the score of blackjack hand of cards
    '''
    if len(hand) < 1:
        raise ValueError('Hand has no cards in it')
    
    score = 0
    ace = False
    for card in hand:
        rank = card[0]
        value = rank
        if rank > 10 and rank != 14:
            value = 10
        if rank == 14:
            ace = True
            value = 11

        if ace:
            if score + value > 21:
                value = 1
        
        score += value
    
    return score


def print_hand_and_score(player_name: str, hand: list):
    '''
    prints the players name, hand, and current score
    '''
    hand = sorted(hand, key = cards.suit_key)
    print(str(player_name), ': ', sep = '')
    print('   ', end = '')
    for card in hand:
        print(card[3], end = ' ')
    print('- score: ', hand_score(hand), sep = '')


def win_lose_or_draw(player_score, dealer_score):
    '''
    Decides the outcome of a game
    '''
    player_busted = False
    dealer_busted = False

    if player_score > 21:
        player_busted = True
    if dealer_score > 21:
        dealer_busted = True

    if player_busted and dealer_busted:
        return 'Draw'
    if player_score == dealer_score:
        return 'Draw'

    if player_busted and not dealer_busted:
        return 'Dealer'
    if dealer_busted and not player_busted:
        return 'Player'

    if player_score > dealer_score:
        return 'Player'
    if dealer_score > player_score:
        return 'Dealer'


def dealer_hit_or_stand(player_hand, dealer_hand):
    '''
    Algorithm that decides whether the dealer hits or stands
    if the dealer should hit, return True
    '''
    player_score = hand_score(player_hand)
    dealer_score = hand_score(dealer_hand)
    if player_score <= 21:
        if dealer_score < 17 or dealer_score < player_score:
            return True
    return False


def player_hit_or_stand():
    '''
    Asks the player if they want to hit or stand
    if the player hits, return True
    '''
    while True:
        play = input('Hit(H) or Stand(S): ').lower()

        if play == 'h':
            return True
        if play == 's':
            return False


def main():
    '''
    makes and plays a game of blackjack.
    '''
    dealer_name = 'Dealer'
    player_name = input('What is your name: ')
    print()
    deck = cards.make_deck(shuffle_deck = True)
    top_half, bottom_half = cards.cut(deck)
    
    player_hand, dealer_hand = cards.deal(bottom_half, 2)

    print_hand_and_score(player_name, player_hand)
    print_hand_and_score(dealer_name, dealer_hand)
    print()
    
    if player_hit_or_stand():
        print('Player hits...')
        player_hand.append(cards.draw(bottom_half))
        print_hand_and_score(player_name, player_hand)
        print()
    else:
        print('Player stands...')

    if dealer_hit_or_stand(player_hand, dealer_hand):
        print('Dealer hits...')
        dealer_hand.append(cards.draw(bottom_half))
        print_hand_and_score(dealer_name, dealer_hand)
    else:
        print('Dealer stands...')

    player_score = hand_score(player_hand)
    dealer_score = hand_score(dealer_hand)
    result = win_lose_or_draw(player_score, dealer_score)
    if result != 'Draw':
        print()
        print(result, 'Wins!')
    else:
        print()
        print(result)
    
    # Manual print_hand_and_score tests
    '''
    hand = [cards.make_card(14, 'Hearts'), cards.make_card(10, 'Diamonds')]
    print_hand_and_score('Kamron', hand)

    hand = [cards.make_card(14, 'Hearts'), cards.make_card(14, 'Clubs')]
    print_hand_and_score('John', hand)

    hand = [cards.make_card(4, 'Hearts'), cards.make_card(2, 'Spades')]
    print_hand_and_score('Jack', hand)
    '''

    # Manual win_lose_or_draw tests
    '''
    print(win_lose_or_draw(10, 10)) # Draw
    print(win_lose_or_draw(22, 22)) # Draw

    print(win_lose_or_draw(22, 21)) # Dealer
    print(win_lose_or_draw(0, 10))  # Dealer

    print(win_lose_or_draw(21, 22)) # Player
    print(win_lose_or_draw(10, 0))  # Player
    '''

    # Manual player_hit_or_stand tests
    '''
    print(player_hit_or_stand())
    '''


if __name__ == "__main__":
    main()
