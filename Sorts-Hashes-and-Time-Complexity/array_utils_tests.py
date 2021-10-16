'''
Author: Kamron Cole
array_utils_tests.py that was created for assignment 6.1 (updated for assignment 7.2)
contains all the tests for array_utils.py
'''
import array_utils
import arrays
import random
from testing import *

def range_array_test():
    '''
    Makes sure range_array returns the proper array (length and values) if only 1 value
    '''
    array = array_utils.range_array(0, 1)
    assert_equals('Length:', 1, len(array), True)

    index = 0
    while index < len(array):
        assert_equals('Index ' + str(index), index, array[index], True)
        index += 1

def range_array_test_2():
    '''
    Makes sure range_array returns the proper array (length and values)
    Values should be in ascending order.
    '''
    array2 = array_utils.range_array(0, 10)
    assert_equals('Length:', 10, len(array2), True)

    index = 0
    while index < len(array2):
        assert_equals('Index ' + str(index), index, array2[index], True)
        index += 1


def random_array_test():
    '''
    Makes sure random_array returns the proper array (length and values) if only 1 value
    '''
    random.seed(1)
    array2 = array_utils.random_array(1, 0, 100)
    assert_equals('Length:', 1, len(array2), True)

    index = 0
    random.seed(1) # Need the second seed call to reset its position to the beginning of the string of numbers thing
    while index < len(array2):
        assert_equals('Index ' + str(index), random.randint(0, 100), array2[index], True)
        index += 1


def random_array_test_2():
    '''
    Makes sure random_array returns the proper array (length and values)
    '''
    random.seed(1)
    array2 = array_utils.random_array(6, 0, 100)
    assert_equals('Length:', 6, len(array2), True)

    index = 0
    random.seed(1) # Need the second seed call to reset its position to the beginning of the string of numbers thing
    while index < len(array2):
        assert_equals('Index ' + str(index), random.randint(0, 100), array2[index], True)
        index += 1


def is_sorted_test():
    '''
    If array is empty it should return as sorted
    '''
    array = arrays.Array(0)
    print('   ', array)
    result = array_utils.is_sorted(array)
    assert_equals('Sorted', True, result, True)


def is_sorted_test_2():
    '''
    If array has 1 value it should return as sorted
    '''
    array = array_utils.range_array(0, 1)
    print('   ', array)
    result = array_utils.is_sorted(array)
    assert_equals('Sorted', True, result, True)


def is_sorted_test_3():
    '''
    range_array should be sorted by default
    '''
    array = array_utils.range_array(0, 10, 1)
    print('   ', array)
    result = array_utils.is_sorted(array)
    assert_equals('Sorted', True, result, True)


def is_sorted_test_4():
    '''
    random_array should return a non-sorted array with seed 0
    '''
    random.seed(0)
    array = array_utils.random_array(10, 1, 100)
    print('   ', array)
    result = array_utils.is_sorted(array)
    assert_equals('Sorted', False, result, True)


def shuffle_test():
    '''
    Makes sure shuffle returns the proper array (length and values)
    '''
    array = array_utils.range_array(0, 10)
    
    random.seed(1)
    shuffled_array = array_utils.shuffle(array)

    # Uses the same shuffle algorithm to test if shuffle shuffled correctly
    test_shuffle_array = array_utils.range_array(0, 10)
    random.seed(1)
    for index in range(0, len(test_shuffle_array)):
        random_index = random.randint(0, len(test_shuffle_array) - 1)
        swap_values_1 = test_shuffle_array[index]
        swap_values_2 = test_shuffle_array[random_index]

        test_shuffle_array[index] = swap_values_2
        test_shuffle_array[random_index] = swap_values_1

    print('   Original Array:', array)
    print('   Shuffled Array:', shuffled_array)
    print('   Test Array(sh):', test_shuffle_array)

    assert_equals('Length', len(array), len(shuffled_array), True)

    i = 0
    while i < len(shuffled_array):
        assert_equals('Index ' + str(i), test_shuffle_array[i], shuffled_array[i], True)
        i += 1


def create_array_test():
    '''
    Uses a test file to make sure create_array creates an array with proper values
    '''
    result = array_utils.create_array('data/create_array_test_file.txt')
    assert_equals('Created array', '[1, 3, 5, 6, 9]', str(result), True)


def copy_array_test():
    '''
    Makes sure the the copies array is the same as the original (length and values)
    '''
    array = array_utils.random_array(10, 0, 100)
    copy_array = array_utils.copy_array(array)
    assert_equals('Length', len(array), len(copy_array), True)
    assert_equals('Copied array', str(array), str(copy_array), True)


def percent_unsorted_test():
    '''
    Creates a half unsorted array and makes sure it returns 50% unsorted
    '''
    array = arrays.Array(6)
    array[0] = 10
    array[1] = 9
    array[2] = 8
    array[3] = 1
    array[4] = 2
    array[5] = 3
    result = array_utils.percent_unsorted(array)
    assert_equals('Percent of array sorted', 50, result, True)


def run_all_tests():
    ''''
    Runs all test using testing.py helper function
    '''
    run_test(range_array_test)
    run_test(range_array_test_2)
    run_test(random_array_test)
    run_test(random_array_test_2)
    run_test(is_sorted_test)
    run_test(is_sorted_test_2)
    run_test(is_sorted_test_3)
    run_test(is_sorted_test_4)
    run_test(shuffle_test)
    run_test(create_array_test)
    run_test(copy_array_test)
    run_test(percent_unsorted_test)


run_all_tests()
