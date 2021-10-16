'''
Author: Kamron Cole
Plots 3 graphs comparing sort times of 2 different sort algorithms
'''
import plotter
import array_utils
import time
import random
from sorts import *

SCALAR = 25
RUNS = 50

def sort_timer(array, sort_function):
    '''
    Returns the time it takes for the given sort function to sort the given array
    '''
    start = time.perf_counter()
    sort_function(array)
    stop = time.perf_counter()
    delta = stop - start
    return delta


def time_sorted(sort_function):
    '''
    Adds data points for the time it takes the given sort function to sort through an already sorted array
    Best case scenario
    '''
    for run in range(RUNS):
        array = array_utils.range_array(0, run * SCALAR)
        plotter.add_data_point(sort_timer(array, sort_function))


def time_random(sort_function):
    '''
    Adds data points for the time it takes the given sort function to sort through a random array
    Average scenario
    '''
    for run in range(RUNS):
        random.seed(100)
        array = array_utils.random_array(run * SCALAR)
        plotter.add_data_point(sort_timer(array, sort_function))


def time_reverse(sort_function):
    '''
    Adds data points for the time it takes the given sort function to sort through an array in reverse sorted order
    Worst case scenario
    '''
    for run in range(RUNS):
        array = array_utils.range_array(run * SCALAR, -1, -1)
        plotter.add_data_point(sort_timer(array, sort_function))


def main():
    '''
    Plots 3 separate graphs.
    1st graph plots times for intersion_sort to sort a sorted array, random array, and reverse array
    2nd graph plots times for bubble_sort to sort a sorted array, random array, and reverse array
    3rd graph compares the average times (random arrays) for bubble and insertion sort
    '''
    # Insertion sort time comparison
    plotter.init('Sort timer (insertion)', 'Run', 'Time(sec)', False)
    time_sorted(insertion_sort)
    plotter.new_series()
    time_random(insertion_sort)
    plotter.new_series()
    time_reverse(insertion_sort)
    plotter.plot()
    input('Press enter to continue...')

    # Bubble sort time comparison
    plotter.init('Sort timer (bubble)', 'Run', 'Time(sec)', False)
    time_sorted(bubble_sort)
    plotter.new_series()
    time_random(bubble_sort)
    plotter.new_series()
    time_reverse(bubble_sort)
    plotter.plot()
    input('Press enter to continue...')

    # Bubble vs Insertion average time comparison
    plotter.init('Sort timer (insertion vs bubble)', 'Run', 'Time(sec)', False)
    time_random(insertion_sort)
    plotter.new_series()
    time_random(bubble_sort)
    plotter.plot()
    input('Press enter to continue...')

    # Start of Manual tests for each function
    # Manual sort_timer tests
    '''
    array = array_utils.range_array(100, -1, -1)
    print(sort_timer(array, bubble_sort))

    array = array_utils.range_array(100, -1, -1)
    print(sort_timer(array, insertion_sort))
    '''

    # Manual time_sorted tests
    '''
    plotter.init('Sort timer (sorted, insertion)', 'Run', 'Time(sec)')
    time_sorted(insertion_sort)
    plotter.plot()
    input()

    plotter.init('Sort timer (sorted, bubble)', 'Run', 'Time(sec)')
    time_sorted(bubble_sort)
    plotter.plot()
    input()
    '''

    # Manual time_random tests
    '''
    plotter.init('Sort timer (random, insertion)', 'Run', 'Time(sec)')
    time_random(insertion_sort)
    plotter.plot()
    input()

    plotter.init('Sort timer (random, bubble)', 'Run', 'Time(sec)')
    time_random(bubble_sort)
    plotter.plot()
    input()
    '''

    # Manual time_reverse tests
    '''
    plotter.init('Sort timer (reverse, insertion)', 'Run', 'Time(sec)')
    time_reverse(insertion_sort)
    plotter.plot()
    input()

    plotter.init('Sort timer (reverse, bubble)', 'Run', 'Time(sec)')
    time_reverse(bubble_sort)
    plotter.plot()
    input()
    '''


if __name__ == "__main__":
    main() # Runs code in main if sort_timer.py is ran directly (not from import)
