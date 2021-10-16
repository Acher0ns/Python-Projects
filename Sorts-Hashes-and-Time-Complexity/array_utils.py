"""
Various utilities for creating and manipulating arrays.

@author GCCIS Faculty
"""

import arrays
import random

def range_array(start, stop, step=1):
    """
    Creates and returns an array from the specified range.
    """
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def random_array(size, min_value=0, max_value=None):
    """
    Creates an array of the specified size with random values ranging from 
    min_value to max_value. Values may be repeated.
    """
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)
    
    return an_array

def is_sorted(an_array):
    """
    Returns True if the array is sorted in increasing order, and False 
    otherwise.
    """
    length = len(an_array)
    if length <= 1:
        return True

    for index in range(1, len(an_array)):
        if an_array[index] < an_array[index-1]:
            return False
    return True

def shuffle(an_array):
    """
    Shuffles the elements in the array into a random order.
    """
    length = len(an_array)
    for i in range(length):
        j = random.randint(0, length-1)
        temp = an_array[i]
        an_array[i] = an_array[j]
        an_array[j] = temp
    
    return an_array

def create_array(filename):
    '''
    Create an array from a file.
    First line is the array length
    After that, 1 array value per line.
    '''
    with open(filename) as file:
        size = int(next(file))
        new_array = arrays.Array(size)
        i = 0 
        for line in file:
            line = line.strip()
            if len(line) > 0:
                new_array[i] = int(line)
                i+=1
    return new_array


def copy_array(array):
    '''
    Returns a copy of the original array
    '''
    result = arrays.Array(len(array))
    for i in range(len(array)):
        result[i] = array[i]
    return result


def array_cat(array1, array2):
    array = arrays.Array(len(array1) + len(array2))

    index = 0
    for i in range(len(array1)):
        array[index] = array1[i]
        index += 1

    for i in range(len(array2)):
        array[index] = array2[i]
        index += 1
    return array


def percent_unsorted(array):
    '''
    Returns how much of an array is unsorted
    '''
    length = len(array)
    unsorted = 0
    if length <= 1:
        return True

    for index in range(1, len(array)):
        if array[index] < array[index - 1]:
            unsorted += 1
    return unsorted / length * 100
    
