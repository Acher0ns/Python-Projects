'''
Author: Kamron Cole
Plots a graph directly comparing insertion, bubble, and merge sort timings using different case scenarios
'''
import arrays
import array_utils
import time
import plotter
import quicksort_ip
from sorts import *
from hybrid_sort import *



def sort_timer(array, sort_function):
    '''
    Returns the time it takes for the given sort function to sort the given array
    '''
    start = time.perf_counter()
    sort_function(array)
    stop = time.perf_counter()
    delta = stop - start
    return delta


def plot_sort_time(array, sort_function):
    '''
    Adds a data point for the time it takes the given sort function to sort through the given array
    '''
    copy_array = array_utils.copy_array(array)
    plotter.add_data_point(sort_timer(copy_array, sort_function))


def plot_times(sort_function, random_array, sorted_array, reverse_array, double_array, mostly_sorted_array):
    '''
    Plot how long it takes for the sort function to sort different types of arrays
    '''
    plot_sort_time(random_array, sort_function) # Average Case
    plot_sort_time(sorted_array, sort_function) # Best Case
    plot_sort_time(reverse_array, sort_function) # Worse Case
    plot_sort_time(double_array, sort_function)
    plot_sort_time(mostly_sorted_array, sort_function)


def create_various_arrays():
    '''
    Helper function that returns all the types of arrays needed for plot_times
    '''
    randmon_array = array_utils.create_array('data/random.txt')
    sorted_array = array_utils.create_array('data/sorted.txt')
    reverse_array = array_utils.create_array('data/reverse.txt')
    double_array = array_utils.create_array('data/two_lists.txt')
    mostly_sorted_array = array_utils.create_array('data/mostly_sorted.txt')

    return randmon_array, sorted_array, reverse_array, double_array, mostly_sorted_array


def main():
    '''
    Plots a graph directly comparing insertion, bubble, and merge sort timings using different case scenarios
    '''
    randmon_array, sorted_array, reverse_array, double_array, mostly_sorted_array = create_various_arrays()

    plotter.init('Plot Time Comparison', 'Array Type', 'Time(sec)')

    # Plot intersion sort times for the 5 array types
    plot_times(insertion_sort, randmon_array, sorted_array, reverse_array, double_array, mostly_sorted_array)
    plotter.new_series()

    # Plot bubble sort times for the 5 array types
    plot_times(bubble_sort, randmon_array, sorted_array, reverse_array, double_array, mostly_sorted_array)
    plotter.new_series()

    # Plot merge sort times for the 5 array types
    plot_times(merge_sort, randmon_array, sorted_array, reverse_array, double_array, mostly_sorted_array)
    plotter.new_series()

    # Plot quicksort_ip sort times for the 5 array types
    plot_times(quicksort_ip.quicksort, randmon_array, sorted_array, reverse_array, double_array, mostly_sorted_array)
    plotter.new_series()

    # Plot hybrid sort times for the 5 array types
    plot_times(hybrid_sort, randmon_array, sorted_array, reverse_array, double_array, mostly_sorted_array)

    plotter.plot(log = True)
    input('Press enter to continue...')


    # plot_sort_time  manual test
    '''
    array = array_utils.range_array(0, 100)
    plotter.init('plot_sort_time test', 'Run', 'Time(sec)', False)
    plot_sort_time(array, insertion_sort)
    plotter.plot()
    input()
    '''

    # plot_times manual test
    '''
    randmon_array = array_utils.create_array('data/random.txt')
    sorted_array = array_utils.create_array('data/sorted.txt')
    reverse_array = array_utils.create_array('data/reverse.txt')
    double_array = array_utils.create_array('data/two_lists.txt')
    mostly_sorted_array = array_utils.create_array('data/mostly_sorted.txt')

    plotter.init('plot_times test', 'Array Type', 'Time(sec)')
    plot_times(sorts.bubble_sort, randmon_array, sorted_array, reverse_array, double_array, mostly_sorted_array)
    plotter.plot()
    input()
    '''


if __name__ == "__main__":
    main() # Runs the code in main if this file is ran directly (not from import)
