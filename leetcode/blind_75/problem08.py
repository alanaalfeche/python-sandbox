'''Problem 23: Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    '''We use heap to keep a list of nodes in priority order at all times. 
    
    List can also be used for this problem but it requires sort() and reverse() after building the list. 
    '''
    heap = []
    for l in lists:
        while l:
            heappush(heap, l.val)
            l = l.next
    head = dummy = ListNode(None)
    while heap:
        dummy.next = ListNode(heappop(heap))
        dummy = dummy.next
    return head.next


l1 = None
for i in 5, 4, 1:
    node = ListNode(i)
    node.next = l1
    l1 = node

l2 = None
for i in 4, 3, 1:
    node = ListNode(i)
    node.next = l2
    l2 = node

l3 = None
for i in 6, 2:
    node = ListNode(i)
    node.next = l3
    l3 = node

answer = merge_k_lists([l1, l2, l3])
for _ in range(8):
    print(answer.val)
    answer = answer.next