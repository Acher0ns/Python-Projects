import sorts
import arrays
import random
import array_utils
from testing import *


def split_test():
    array = arrays.Array(6)
    array[0] = 5
    array[1] = 4
    array[2] = 3
    array[3] = 2
    array[4] = 1
    array[5] = 0

    half1 = arrays.Array(3)
    half1[0] = 5
    half1[1] = 3
    half1[2] = 1

    half2 = arrays.Array(3)
    half2[0] = 4
    half2[1] = 2
    half2[2] = 0

    result1, result2 = sorts.split(array)

    assert_equals('Half 1', str(half1), str(result1), True)
    assert_equals('Half 2', str(half2), str(result2), True)


def merge_test():
    half1 = arrays.Array(3)
    half1[0] = 5
    half1[1] = 3
    half1[2] = 1

    half2 = arrays.Array(3)
    half2[0] = 4
    half2[1] = 2
    half2[2] = 0

    merged_array = arrays.Array(6)
    merged_array[0] = 4
    merged_array[1] = 2
    merged_array[2] = 0
    merged_array[3] = 5
    merged_array[4] = 3
    merged_array[5] = 1

    result = sorts.merge(half1, half2)

    assert_equals('Merged array', str(merged_array), str(result), True)


def merge_sort_empty_test():
    array = arrays.Array(0)
    result = sorts.merge_sort(array)
    assert_equals('Merge Sort empty', array, result, True)


def merge_sort_length1_test():
    array = arrays.Array(1)
    result = sorts.merge_sort(array)
    assert_equals('Merge Sort empty', array, result, True)


def merge_sort_test():
    random.seed(1)
    array = array_utils.random_array(5, 0, 100)
    result = sorts.merge_sort(array)

    random.seed(1)
    array_sorted = array_utils.random_array(5, 0, 100)
    sorts.insertion_sort(array_sorted)

    assert_equals('Sorted Array', str(array_sorted), str(result), True)


def run_all_tests():
    run_test(split_test)
    run_test(merge_test)

    run_test(merge_sort_empty_test)
    run_test(merge_sort_length1_test)
    run_test(merge_sort_test)


run_all_tests()