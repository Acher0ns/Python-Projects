import sorts
import arrays
import random
import array_utils
from testing import *

def quicksort_sort_empty_test():
    array = arrays.Array(0)
    result = sorts.quicksort_sort(array)
    assert_equals('Quicksort sort empty', array, result, True)


def quicksort_sort_length1_test():
    array = arrays.Array(1)
    result = sorts.quicksort_sort(array)
    assert_equals('Quicksort sort empty', array, result, True)


def quicksort_sort_test():
    random.seed(1)
    array = array_utils.random_array(5, 0, 100)
    result = sorts.quicksort_sort(array)

    random.seed(1)
    array_sorted = array_utils.random_array(5, 0, 100)
    sorts.insertion_sort(array_sorted)

    assert_equals('Sorted Array', str(array_sorted), str(result), True)


def run_all_tests():
    run_test(quicksort_sort_empty_test)
    run_test(quicksort_sort_length1_test)
    run_test(quicksort_sort_test)


run_all_tests()