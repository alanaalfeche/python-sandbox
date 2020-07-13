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
    for i in range(len(alist)):
        key = alist[i]
        idx = i - 1

        while idx >= 0 and alist[idx] > key:
            alist[idx+1] = alist[idx]
            idx -= 1
        
        alist[idx + 1] = key

    return alist

def gap_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        key = alist[i]
        idx = i

        while idx >= gap and alist[idx-gap] > key:
            alist[idx] = alist[idx-gap]
            idx = idx - gap

        alist[idx] = key

    return alist

def shell_sort(alist):
    """
    A version of insertion sort where gap-indexed values is sorted where gap = len(sublist/x), usually x = 2. 
    Shell sort is said to be unstable because swapping is involved so original order is not conserved. 
    Average complexity varies between O(n^3/2) and O(n^5/2) with a worst complexity of O(n^2).
    """
    sublist_count = len(alist) // 2
    while sublist_count > 0:
        for i in range(sublist_count):
            gap_insertion_sort(alist, i, sublist_count)
        sublist_count = sublist_count // 2

    return alist

def merge(left, right):
    result = []
    i, j = 0, 0 
    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(alist):
    """
    Merge sort is a divide-and-conquer algorithm with a worst case of O(n log n) time. 
    `log n` from splitting the unsorted list into n sublits, each containing one element 
    `n` from repeatedly merging sublists to produce new sorted sublits until there is only one sorted list remaining.  
    """
    if len(alist) < 2:
        return alist
    else:
        mid = len(alist) // 2
        left = merge_sort(alist[:mid])
        right = merge_sort(alist[mid:])
        return merge(left, right)

def main():
    alist = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
    bb = bubble_sort(alist)
    sl = selection_sort(alist)
    ts = insertion_sort(alist)
    ss = shell_sort(alist)
    ms = merge_sort(alist)

    if bb == sl == ts == ss == ms:
        print('Success!')

main()