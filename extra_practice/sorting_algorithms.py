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

def insertion_sort(alist):
    """
    Also an in-place sorting algorithm where it creates a sorted list to the left as it iterates through the list to the right. 
    Similar to bs and ss, it also have a complexity of O(n^2).  
    """
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1

        while j >= 0 and alist[j] > key:
            alist[j+1] = alist[j]
            j -= 1
        
        alist[j + 1] = key

    return alist

def main():
    alist = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
    bb = bubble_sort(alist)
    ss = selection_sort(alist)
    ts = insertion_sort(alist)

    if bb == ss == ts:
        print('Success!')

main()