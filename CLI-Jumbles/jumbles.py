'''
Author: Kamron Cole
jumbles.py originally created for assignment 10.2
Prompts the user to input clues for a jumble and will find the end solution
Also contains functions to auto solve jumbles by reading inputs from a file
'''

DATA_PATH = '/Users/Kamron/Documents/GitHub/SoftDevI/Unit10/Day01-03/data/'

# Global ANSI color variables used to print errors and when printing results
RED = '​\033[31m​'
GREEN = '\033[92m'
WHITE = '​\033[37m​'

def dictionary(filename: str) -> list:
    '''
    Creates a dictionary(list) or words from a file given 1 word per line
    '''
    words = []
    with open(filename) as file:
        for line in file:
            word = line.strip()
            words.append(word.lower())
    return words


def letters_in_word(word: str) -> str:
    '''
    Sorts the letters in a word and returns them as a string
    '''
    result = ''
    letters = sorted(list(word.lower()))
    for char in letters:
        result += char
    return result


def jambles(words: list) -> dict:
    '''
    creates a dictionary containing solutions for word scrambles
    '''
    jambles = {}
    for word in words:
        sorted_word = letters_in_word(word)
        if sorted_word not in jambles:
            jambles[sorted_word] = [word]
            continue
        jambles[sorted_word].append(word)
    return jambles


def find_solution_in_dict(letters: str, solutions: dict):
    '''
    Searches a dict(usually made from jambles) for the key or sorted letters
    if it exists it either returns the result if there is only one or asks the user to choose from a list of results
    '''
    found = False
    sorted_letters = letters_in_word(letters)
    for key in solutions:
        if key == sorted_letters:
            solutions = solutions[key]
            found = True
            break

    if not found:
        print('"' + letters + '" has no possible solutions.')
        return None
    
    if len(solutions) == 1:
        return solutions[0]
    
    while True:
        for i in range(len(solutions)):
            print(i, ': ', solutions[i], sep = '')

        try:
            choice = int(input('Enter the index of a word: '))
            return solutions[choice]
        except IndexError:
            print()
            print(RED + 'Please enter a valid choice: ', 0, ' - ', len(solutions) - 1, '.' + WHITE, sep = '')
            print()
        except ValueError:
            print()
            print(RED + 'Please enter a number.' + WHITE)
            print()


def prompt_for_clue():
    '''
    promts the user to input a clue in the format 'scrambled_letter index*'
    * = as many indecies they want
    no quotes should be in the input of coarse
    '''
    while True:
        solution_letters = ''
        problem = input('Enter scramble and indexes of solution letter:\n')
        args = problem.split()

        scramble = args[0]
        solution_word = find_solution_in_dict(scramble, jambles(dictionary(DATA_PATH + 'words.txt')))

        try:
            for element in args[1:]:
                index = int(element)
                solution_letters += solution_word[index]
            return solution_word, solution_letters
        except ValueError:
            print()
            print(RED + 'Please enter a valid number' + WHITE)
            print()
        except IndexError:
            print()
            print(RED + 'Letter indexes are out of range of the scramble:' + WHITE, scramble)
            print()


'''
Assignment Question 7 work except no prompting the user and gets the question from the .puz file
'''
def auto_solve_jumble(question: str, clues: str):
    '''
    Contains the logic for auto solving jumbles using a string of clues created from a file
    could be simplified but i dont have much time :)
    '''
    solutions = jambles(dictionary(DATA_PATH + 'words.txt')) # Creates the dict of solutions
    solution_letters = ''
    clues = clues.split('\n') # splits the clues into a list, each element being a clue or an index denoting a word choice

    final_solution_letters = ''

    search_index = 0
    for clue in clues[:-1]: # last value in clues is an empty string
        if len(clue) != 1: # if clue is not denoting an index of a word choice
            solution_letters = ''
            scramble = clue.split()[0] # scrambled letters should be the first element in clue.split
            solution_word = ''
            if len(clues[search_index + 1]) == 1: # if next element in clues contains only 1 value it is denoting an index meaning this scramble has multiple solutions
                solution_word = find_solution_multi_auto(scramble, solutions, clues[search_index + 1]) # Chooses the correct word given the word index that is the next element of clues
            else:
                solution_word = find_solution_single(scramble, solutions)
                
            for element in clue.split()[1:]: # first element in clue is the scramble after that is a bunch of indecies denoting letters for the final solution
                index = int(element)
                solution_letters += solution_word[index]
            final_solution_letters += solution_letters # adds this iterations solution letters to the final solution
        search_index += 1

    final_solution_word = find_solution_multi_auto(final_solution_letters, solutions, clues[search_index - 1]) # Finds the solution of the jumble
    print('question:', question)
    print('solution:', final_solution_word)
    print()


def find_solution_multi_auto(letters: str, solutions: dict, index: int):
    '''
    Searches a dict(usually made from jambles) for the key or sorted letters
    if it exists it either returns the result if there is only one or returns the result from a list of results at the given index
    '''
    found = False
    sorted_letters = letters_in_word(letters)
    for key in solutions:
        if key == sorted_letters:
            solutions = solutions[key]
            found = True
            break

    if not found:
        print('"' + letters + '" has no possible solutions.')
        return None
    
    if len(solutions) == 1:
        return solutions[0]
    
    choice = int(index)
    return solutions[choice]


def find_solution_single(letters: str, solutions: dict):
    '''
    Searches a dict(usually made from jambles) for the key or sorted letters
    returns the result if there is only one
    '''
    found = False
    sorted_letters = letters_in_word(letters)
    for key in solutions:
        if key == sorted_letters:
            solutions = solutions[key]
            found = True
            break

    if not found:
        print('"' + letters + '" has no possible solutions.')
        return None
    
    if len(solutions) == 1:
        return solutions[0]
        

def get_jumble_from_file(puzzle_name):
    '''
    Given a jumble puzzle name, finds the .puz and .sol files of the puzzle and returns the question and the clues in the .sol used to solve the puzzle
    '''
    puz_filename = puzzle_name + '.puz'
    sol_filename = puzzle_name + '.sol'

    question = ''
    with open(puz_filename) as puz_file:
        question = next(puz_file).strip()
        puz_file.close()

    clues = ''
    with open(sol_filename) as sol_file:
        for line in sol_file:
            line = line.strip()
            clues += line + '\n'

    return question, clues


def main():
    '''
    Main function

    Prompts the user to input 4 clues for a jumble and will find solutions for those clues
    Then will find an end solution
    '''
    words_small = dictionary(DATA_PATH + 'words_small.txt')
    words = dictionary(DATA_PATH + 'words.txt')
    solutions_small = jambles(words_small)
    solutions = jambles(words)

    final_solution_letters = ''
    for i in range(4):
        solution_word, solution_letters = prompt_for_clue()
        print(GREEN + 'word:', solution_word + WHITE)
        final_solution_letters += solution_letters
        print()

    final_solution_word = find_solution_in_dict(final_solution_letters, solutions)
    print(GREEN + 'solution:', final_solution_word + WHITE)


    # Manual dictionary tests
    # print(words_small)

    # Manual jambles tests
    # print(jambles(words_small))

    # Manual find_solution_in_dict tests
    # print(find_solution_in_dict('UNBRAU', jambles(words_large)))

    # Manual prompt_for_clue test
    # print(prompt_for_clue())

    # Question 7 prompts
    question, clues = get_jumble_from_file(DATA_PATH + 'jumble001')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble002')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble003')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble004')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble005')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble006')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble007')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble008')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble009')
    auto_solve_jumble(question, clues)

    question, clues = get_jumble_from_file(DATA_PATH + 'jumble010')
    auto_solve_jumble(question, clues)


if __name__ == "__main__":
    main() # pragma: no cover
