'''
Author: Kamron Cole
Originally created for assignment 10.3
Analyzes the effectiveness different types of hash functions
'''
import random
import arrays
import array_utils

def very_bad_hash(string):
    '''
    Returns the same value no matter the string input.
    This has function is very bad hashing function.
    Always results in collisions therefore its speed is O(n) and input. 
    Given the same or different input it always returns the same output.
    '''
    return 0


def inconsistent_hash(string):
    '''
    Returns a random hash no matter the input.
    This hash function is fast but can result in multiple collisions making it lean towards O(n)
    Very inconsistent, same inputs are most likely to have different hashes
    '''
    return random.randint(0, 1000)


def sum_ascii_hash(string):
    '''
    Returns the sum of the ascii codes of the letters in a string as the hash.
    This hash function is fast but can result in multiple collisions making it lean towards O(n)
    Results in more collisions than inconsistent_hash. Collisions occure from strings with similar letters.
    Will return same value for the same input.
    '''
    hash_code = 0
    for letter in string:
        hash_code += ord(letter)
    return hash_code


def better_hash(string):
    '''
    Returns the sum of the ascii code of a letter times 31 ^ length of the input - (1 + index of the letter).
    Is consistent. Will return the same hash for the input
    Is Fast.
    Few collisions. Due to the algorithm, hash is dependent on the order of letters in the input.
    '''
    exponent = len(string) - 1
    hash_code = 0
    for char in string:
        hash_code += ord(char) * 31 ** exponent
        exponent -= 1
    return hash_code


def count_collisions(hash_func, length):
    '''
    Counts number of collisions a hash_function returns.
    Creates a list of the specified length and then hashes every possible 3 lowercase letter combination.
    Iterates through the hashes and calculates an index for that hash. 
    Then adds 1 to collisions_list at that index counting how many values have been placed at that same index.
    Prints total number of collisions and the average number of collision over all indices.
    '''
    print('hashing ', length, ' items using ', hash_func.__name__, '...', sep = '')
    collisions_list = [0 for i in range(length)]
    hashes = [hash_func(chr(i) + chr (j) + chr(k)) for i in range(97, 123) for j in range(97, 123) for k in range(97, 123)]
    for hash_code in hashes:
        index = hash_code % length
        collisions_list[index] += 1

    total_collisions = 0
    count = 0
    for element in collisions_list:
        if element > 1:
            total_collisions += element - 1

        if element > 0:
            count += 1

    print('  total collisions:', total_collisions)
    print('  average collisions:', total_collisions / count)
    print('finished.')


def hash_func_analysis(hash_func):
    '''
    Uses count_collisions to analyze a hash function using various list sizes
    '''
    print('Running test 1 of ', hash_func.__name__, ':', sep = '')
    count_collisions(hash_func, 100)

    print('Running test 2 of ', hash_func.__name__, ':', sep = '')
    count_collisions(hash_func, 1000)

    print('Running test 3 of ', hash_func.__name__, ':', sep = '')
    count_collisions(hash_func, 10000)

    print('Running test 4 of ', hash_func.__name__, ':', sep = '')
    count_collisions(hash_func, 100000)


def main():
    '''
    Uses hash_func_analysis to analyze hash functions using various list lengths

    Python's built in hash function is fast and consistent.
    However, provides more collisions that better_hash.
    '''
    hash_func_analysis(very_bad_hash)

    print()
    print()

    hash_func_analysis(inconsistent_hash)

    print()
    print()

    hash_func_analysis(sum_ascii_hash)

    print()
    print()

    hash_func_analysis(better_hash)

    print()
    print()

    hash_func_analysis(hash)
    
    '''
    # Manual tests for hash_func_analysis helper function
    hash_func_analysis(very_bad_hash)
    '''


if __name__ == "__main__":
    main()
