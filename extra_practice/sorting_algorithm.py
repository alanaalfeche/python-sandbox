# Sorting Algorithms

def bubble_sort(alist):
    """
    In-place sorting algorithm that has an average complexity of O(n^2). 
    Algorithm that generates the most "swaps" but can be efficient if list is sorted. 
    We can also the "swaps" as an indicator that a list is sorted. 
    """
    for i in range(len(alist)):
        for j in range(len(alist)-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

print(bubble_sort([19, 13, 6, 2, 18, 8]))

def selection_sort(alist):
    """
    Another in-place sorting algorithm like bubble with a worst, best, and average complexity of O(n^2).
    But, it makes the most minimum swap of n-1. 
    For ever pass, ss looks for index with the most minimum value and makes a swap with current min value if found. 
    """
    size = len(alist)
    for i in range(size):
        min_index = i

        for j in range(i+1, size):
            if alist[j] < alist[min_index]:
                min_index = j

        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist

print(selection_sort([19, 13, 6, 2, 18, 8]))
