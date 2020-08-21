'''Problem 141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 

If pos is -1, then there is no cycle in the linked list.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    '''This algorithm uses fast-slow pattern to determine if there is a cycle in the list. 

    The fast pointer traverses through the single-linked list at a faster rate than the slow pointer, hoping to catch slow at n-traversal. 
    '''
    if not head:
        return False
    l1, l2 = head, head.next
    while l1 and l2 and l2.next:
        if l1 == l2:
            return True
        l1 = l1.next
        l2 = l2.next.next
    return False