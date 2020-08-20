'''Problem 21: Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Solution Authored By NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/problems/problem08.py
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    '''	Move along both linked lists, comparing the nodes at each point and linking the lesser of the two to the return list.'''    
    head = dummy = ListNode(None)
    while l1 and l2:
        if l1.val < l2.val:
            dummy.next = l1
            dummy = l1       
            l1 = l1.next 
        else: 
            dummy.next = l2
            dummy = l2
            l2 = l2.next
    dummy.next = l1 or l2
    return head.next

l1 = None
for i in 4, 2, 1:
    node = ListNode(i)
    node.next = l1
    l1 = node

l2 = None
for i in 4, 3, 1:
    node = ListNode(i)
    node.next = l2
    l2 = node

merge_two_lists(l1, l2)