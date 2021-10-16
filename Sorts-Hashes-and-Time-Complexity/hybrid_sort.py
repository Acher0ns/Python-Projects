from sorts import *
import array_utils
import arrays
import time

def hybrid_sort(array):
    if not array_utils.is_sorted(array):   
        percent_unsorted = array_utils.percent_unsorted(array)  
        if percent_unsorted <= 10:
            if len(array) >= 1000:
                return merge_sort(array)
            else:
                return insertion_sort(array)    
        elif  percent_unsorted > 10 and percent_unsorted < 70:
            return quicksort_ip.quicksort(array)
        else:
            return merge_sort(array)


def main():
    array = array_utils.random_array(1000, 0, 5000)
    hybrid_sort(array)
    print(array)


if __name__ == "__main__":
    main()
