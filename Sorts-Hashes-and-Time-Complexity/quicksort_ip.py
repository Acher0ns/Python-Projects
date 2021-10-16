"""
In-Place Quicksort implementation
"""

import arrays
import array_utils

def swap (a, i, j):
    """
    Swaps the elements i and j within array a
    """
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def quicksort (A):
    """
    Sorts an array in-place, quickly.
    """
    sort (A, 0, len(A) - 1)

def sort (A, lo, hi):
    """
    Recusive quicksort call.
    """
    if lo < hi:
        p = partition (A, lo, hi)
        sort (A, lo, p - 1)
        sort (A, p + 1, hi)

def partition (A, lo, hi):
    """
    Partitions the array into less, same, more segments. 
    This function does not create additional arrays.
    """
    pivot = A[hi]
    i = lo
    for j in range (lo, hi + 1):
        if A[j] < pivot:
            swap (A, i, j)
            i = i + 1
    swap (A, i, hi)
    return i

def main ():
    an_array = array_utils.random_array (100, 0, 1000)
    quicksort (an_array)
    print (an_array)

if __name__ == "__main__":
    main ()
