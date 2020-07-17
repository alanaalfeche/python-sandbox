"""
Problem 23 - Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_list(l1, l2):
    head = dummy = ListNode(None)
    while l1 and l2:
        if l1.val < l2.val:
            dummy.next = l1
            l1 = l1.next 
        else: 
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next
    dummy.next = l1 or l2
    return head.next

def merge_k_lists(lists):
    if len(lists) < 2:
        return lists[0]
    else:
        mid = len(lists) // 2
        left = merge_k_lists(lists[:mid]) # 0, 1      [5, 4, 1]
        right = merge_k_lists(lists[mid:]) # 1, 3     [4, 3, 1] [6, 2]
        return merge_list(left, right)

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