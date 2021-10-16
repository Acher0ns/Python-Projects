'''
Author: Kamron Cole
Originally created for assignment 8.3
A simple game of matching card
'''
import cards
import time

def make_flippable(card: tuple, flipped = False) -> list:
    '''
    Adds a bool property to a card to make it flippable
    '''
    return [card, flipped]


def is_match(flippable1, flippable2):
    '''
    if a card is flipped and the cards are equal then they are a match (return True)
    '''
    flipped = flippable1[1] == True and flippable2[1] == True
    if flippable1 == flippable2 and flipped: return True
    return False


def select_cards(deck, qty):
    '''
    selects half of the qty of cards from the back up the deck and makes a list of them
    then creates a copy of each card so each card has a matching pair
    '''
    if qty % 2 == 1:
        raise IndexError('Quantity cannot be odd: ' + str(qty))
    
    half = qty // 2
    selected = deck[:half]
    return selected + selected


def make_board(rows, columns, deck, shuffle = True):
    '''
    makes the board, a 2D list of cards.
    '''
    selected = select_cards(deck, rows * columns)
    if shuffle: selected = cards.shuffle(selected)

    board = [[make_flippable(selected.pop()) for _ in range(columns)] for _ in range(rows)]
    return board


def remove_card(row, col, board):
    '''
    sets the card a the input row/column of board to and empty string (False)
    '''
    board[row][col] = ['']


def make_face_up(row, col, board):
    '''
    makes a card face-up if its face-down and a valid card (not a removed card).
    '''
    if not board[row][col][0]:
        raise ValueError('Cannot flip a removed card: row: ' + str(row) + 'col: ' + str(col))
    if board[row][col][1]:
        raise ValueError('Card is already face-up')

    board[row][col][1] = True


def make_face_down(row, col, board):
    '''
    makes a card face-down if its face-up and a valid card (not a removed card).
    '''
    if not board[row][col][0]:
        raise ValueError('Cannot flip a removed card: row: ' + str(row) + ', col: ' + str(col))
    if not board[row][col][1]:
        raise ValueError('Card is already face-up')

    board[row][col][1] = False


def print_board(board):
    '''
    prints the board. space inbetween each card 
    face-down cards = '[-]'
    face-up cards = a card's shorthand (ex: '10H')
    removed cards = '   '
    '''
    for row in board:
        for col in row:
            if not col[0]:
                print('   ', end = ' ')
            elif col[1]:
                print(col[0][3], end = ' ')
            else:
                print('[-]', end = ' ')
        print()


def make_move(board):
    '''
    prompts the user to make a move then returns a valid move row and column input
    '''
    while True:
        try:
            row = int(input('Enter a row: '))
            col = int(input('Enter a column: '))
            if board[row][col]:
                return row, col
        except IndexError:
            print()
            print('row or column input was outside the board')
        except ValueError:
            print()
            print('please enter a number')


def main():
    '''
    Main Game
    Uses a loop to create a matching card game.
    Prints board, time, and score every turn. Prints board everytime a card is turned face up.
    Checks if the 2 cards turned face up are matching, if to remove them, if not flip them over
    If no cards are left on the board, print final score and time, then asks the user to play again.
    '''
    while True:
        '''
        Declare rows, cols, and boards here because they are needed in this scope
        '''
        rows = 0
        cols = 0
        board = []

        '''
        Makes sure valid rows/columns are input
        if not, exits the program
        '''
        try:
            rows = int(input('Enter number of board rows: '))
            cols = int(input('Enter number of board columns: '))
            board = make_board(rows, cols, cards.make_deck(True), True)
        except IndexError:
            print()
            print('rows * columns must be even or their wont a proper amount on cards')
            break
        except ValueError:
            print()
            print('please enter a number')
            break
        
        # Variables that need to be reset every game but not every turn, also needed in this scope
        score = 0
        start = time.perf_counter()
        turn = -1
        while True:
            turn += 1

            stop = time.perf_counter()
            print() 
            print()
            print()
            print_board(board)
            print('time:', round((stop - start) - (1.75 * turn), 1)) # prints the time rounded to the first decimal. '- (1.75 * turn)' is because program sleeps for 1.75s at the end of each turn to display the board
            print('score:', score)

            # loop to make sure valid moves are input. if not, retry
            while True:
                move1_row, move1_col = make_move(board)
                try:
                    make_face_up(move1_row, move1_col, board)
                    break
                except ValueError:
                    print('Cannot flip an already flipped or removed card')

            # print the board after a move
            print()
            print()
            print()
            print_board(board)

            # loop to make sure valid moves are input. if not, retry
            while True:
                move2_row, move2_col = make_move(board)
                try:
                    make_face_up(move2_row, move2_col, board)
                    break
                except ValueError:
                    print('Cannot flip an already flipped or removed card')


            # print the board after a move
            print()
            print()
            print()
            print_board(board)

            '''
            checks if the 2 cards flipped over are a match.
            if so, remove them, else, flip them both back over
            '''
            matched = is_match(board[move1_row][move1_col], board[move2_row][move2_col])
            if matched:
                remove_card(move1_row, move1_col, board)
                remove_card(move2_row, move2_col, board)
                score += 1
            else:
                make_face_down(move1_row, move1_col, board)
                make_face_down(move2_row, move2_col, board)

            time.sleep(1.75) # gives the player time to view the move before going to the next turn

            if score == rows * cols / 2: # this is the end game check. score gets +1 for a match, max score is rows * cols / 2. if thats reached, end
                break

        '''
        print final score and time
        '''
        stop = time.perf_counter()
        print('Game over!')
        print('Final Score:', score)
        print('Total Time(seconds):', round(stop - start, 1))
        print()

        time.sleep(3) # gives players time to loop at score
        play_again_prompt = input('Play again? (Y/N): ').lower() # prompts the user to play again
        if play_again_prompt == 'y':
            print()
            continue
        else:
            break


    '''
    Manual Tests
    '''
    # Manual make_board tests
    # board = make_board(2, 2, cards.make_deck(shuffle_deck = True))
    # print(board)

    # Manual remove_card tests
    # remove_card(0, 0, board)
    # print(board)

    # Manual print_board tests
    # remove_card(1, 1, board)
    # make_face_up(0, 0, board)
    # print_board(board)

    # Manual make_move test
    # row, col = make_move(board)
    # print(row, col)


if __name__ == "__main__":
    main() # runs code in main if file is ran directly (not from import)
