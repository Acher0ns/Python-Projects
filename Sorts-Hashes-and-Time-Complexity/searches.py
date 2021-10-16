"""
Python implementations of common search algorithms.

@author GCCIS Faculty
"""
import arrays
import array_utils
import sorts

def linear_search(an_array, target):
    """
    Searches an array for a target value.
    """
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index
    return None


def increasing_comparator(a, b):
    if a >= b:
        return False
    return True


def decreasing_comparator(a, b):
    if a >= b:
        return True
    return False


def binary_search(an_array, target, comparator = increasing_comparator, start=None, end=None):
    """
    An implementation of the binary search algorithm.
    """
    if start == None:
        start = 0
    if end == None:
        end = len(an_array) - 1

    if start > end:
        return None
    else:
        mid = (start + end) // 2
        value = an_array[mid]
        if value == target:
            return mid
        elif comparator(value, target):
            start = mid + 1
            return binary_search(an_array, target, comparator, start, end)
        else:
            end = mid - 1
            return binary_search(an_array, target, comparator, start, end)


def main():
    '''
    array = array_utils.range_array(1000, 1, -1)
    print(array)
    print(binary_search(array, 500))

    print(increasing_comparator(1, 2))
    print(increasing_comparator(2, 1))
    print(decreasing_comparator(1, 2))
    print(decreasing_comparator(2, 1))
    '''
    
    array = array_utils.range_array(0, 1000)
    print(binary_search(array, 100))

    array = array_utils.range_array(1000000, 0, -1)
    print(binary_search(array, 500, decreasing_comparator))


if __name__ == "__main__":
    main()
