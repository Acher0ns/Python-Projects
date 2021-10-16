'''
Author: Kamron Cole
File initially created for 7.1 classwork.
Contains manual tests, sort function, and helper function for said sort functions.
'''
import arrays
import array_utils
import random
import time
import quicksort_ip

def increasing_comparator(a, b):
    '''
    Compares a and b
    if a is greater or equal to b, return false
    if b is less or equal to a, return false

    if a is less than b, return true
    '''
    if a >= b:
        return False
    return True


def decreasing_comparator(a, b):
    '''
    Compares a and b
    if a is greater or equal to b, return true
    if b is less or equal to a, return true

    if a is less than b, return false
    '''
    if a >= b:
        return True
    return False


def swap(array, a, b):
    '''
    Swaps 2 values at a and b in an array
    '''
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def shift(array, index, comparator = increasing_comparator):
    while index > 0:
        if comparator(array[index], array[index - 1]):
            swap(array, index, index - 1)
        else:
            break
        index -= 1


def insertion_sort(array, comparator = increasing_comparator):
    for i in range(len(array)):
        shift(array, i, comparator)


def bubble_sort(array, comparator = decreasing_comparator):
    for j in range(len(array) -1, 0, -1):
        for i in range(j):
            if comparator(array[i], array[i + 1]):
                swap(array, i, i + 1)

'''
Start merge_sort and its helper functions
'''
def split(array):
    half1_length = (len(array) + 1) // 2
    half2_length = len(array) // 2
    evens = arrays.Array(half1_length)
    evens_index = 0
    odds = arrays.Array(half2_length)
    odds_index = 0

    is_even = True
    for i in range(len(array)):
        if is_even:
            evens[evens_index] = array[i]
            evens_index += 1
        else:
            odds[odds_index] = array[i]
            odds_index += 1
        is_even = not is_even
    return evens, odds


def merge(array1, array2):
    length1 = len(array1)
    length2 = len(array2)
    total_length = length1 + length2

    result = arrays.Array(total_length)

    i1 = 0
    i2 = 0
    result_index = 0
    while i1 < length1 and i2 < length2:
        if array1[i1] <= array2[i2]:
            result[result_index] = array1[i1]
            result_index += 1
            i1 += 1
        else:
            result[result_index] = array2[i2]
            result_index += 1
            i2 += 1

    while i1 < length1:
        result[result_index] = array1[i1]
        result_index += 1
        i1 += 1

    while i2 < length2:
        result[result_index] = array2[i2]
        result_index += 1
        i2 += 1
    return result

def merge_sort(array, comparator = increasing_comparator):
    if len(array) == 0:
        return array
    if len(array) == 1:
        return array
    
    half1, half2 = split(array)
    return merge(merge_sort(half1), merge_sort(half2))


'''
Start quicksort_sort and its helper functions
'''
def partition(pivot, array):
    less = arrays.Array(0)
    same = arrays.Array(0)
    more = arrays.Array(0)

    for i in range(len(array)):
        if array[i] < pivot:
            less = array_utils.array_cat(less, arrays.Array(1, array[i]))
        elif array[i] > pivot:
            more = array_utils.array_cat(more, arrays.Array(1, array[i]))
        else:
            same = array_utils.array_cat(same, arrays.Array(1, array[i]))

    return less, same, more


def quicksort_sort(array):
    if len(array) == 0:
        return array

    pivot = array[0]
    less, same, more = partition(pivot, array)
    t1 = quicksort_sort(less)
    t2 = array_utils.array_cat(t1, same)
    t3 = quicksort_sort(more)
    return array_utils.array_cat(t2, t3)


def quicksort_sort_mid(array):
    if len(array) == 0:
        return array

    pivot = array[len(array) // 2]
    less, same, more = partition(pivot, array)
    t1 = quicksort_sort(less)
    t2 = array_utils.array_cat(t1, same)
    t3 = quicksort_sort(more)
    return array_utils.array_cat(t2, t3)


def quicksort_sort_random(array):
    if len(array) < 2:
        return array

    pivot = array[random.randint(0, len(array) - 1)]
    less, same, more = partition(pivot, array)
    t1 = quicksort_sort(less)
    t2 = array_utils.array_cat(t1, same)
    t3 = quicksort_sort(more)
    return array_utils.array_cat(t2, t3)


def quibblesort_sort(an_array):
    if len(an_array) < 10:
        bubble_sort(an_array)
        return an_array

    pivot = an_array[0]
    less, same, more = partition(pivot, an_array)
    new_array = array_utils.array_cat(quicksort_sort(less), same)
    new_array = array_utils.array_cat(new_array, quibblesort_sort(more))
    return new_array


def sort_timer(array, sort_function):
    '''
    Returns the time it takes for the given sort function to sort the given array
    '''
    start = time.perf_counter()
    sort_function(array)
    stop = time.perf_counter()
    delta = stop - start
    return delta


def main():
    sorted_array = array_utils.range_array(0, 10)
    random_array = array_utils.random_array(9, 0, 5000)

    print('quick sort ip race')
    print(sort_timer(sorted_array, quicksort_ip.quicksort))
    print(sort_timer(sorted_array, quicksort_ip.quicksort))
    print(sort_timer(sorted_array, quicksort_ip.quicksort))
    print()
    print(sort_timer(random_array, quicksort_ip.quicksort))
    print(sort_timer(random_array, quicksort_ip.quicksort))
    print(sort_timer(random_array, quicksort_ip.quicksort))
    print()
    print('quick sort non-ip race')
    print(sort_timer(sorted_array, quicksort_sort))
    print(sort_timer(sorted_array, quicksort_sort_mid))
    print(sort_timer(sorted_array, quicksort_sort_random))
    print()
    print(sort_timer(random_array, quicksort_sort))
    print(sort_timer(random_array, quicksort_sort_mid))
    print(sort_timer(random_array, quicksort_sort_random))
    print()
    print('quibble sort race')
    print(sort_timer(sorted_array, quibblesort_sort))
    print(sort_timer(sorted_array, quibblesort_sort))
    print(sort_timer(sorted_array, quibblesort_sort))
    print()
    print(sort_timer(random_array, quibblesort_sort))
    print(sort_timer(random_array, quibblesort_sort))
    print(sort_timer(random_array, quibblesort_sort))



    # Manual Shift Test
    '''
    array = array_utils.range_array(0, 10)
    swap(array, 0, 1)
    print(array)
    shift(array, 1)
    print(array)

    array = array_utils.range_array(10, 0, -1)
    swap(array, 0, 1)
    print(array)
    shift(array, 1, decreasing_comparator)
    print(array)
    '''

    # Manual insertion_sort test
    '''
    array = array_utils.range_array(10, 0, -1)
    print(array)
    insertion_sort(array)
    print(array)

    array = array_utils.range_array(1, 11)
    print(array)
    insertion_sort(array, decreasing_comparator)
    print(array)
    '''

    # Manual bubble_sort test
    '''
    array = array_utils.range_array(10, 0, -1)
    print(array)
    bubble_sort(array)
    print(array)

    array = array_utils.range_array(1, 11)
    print(array)
    bubble_sort(array, increasing_comparator)
    print(array)
    '''
    

if __name__ == "__main__":
    main() # Runs code in main if sorts.py is ran directly (not from import)
