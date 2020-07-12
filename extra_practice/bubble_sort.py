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