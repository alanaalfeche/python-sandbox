'''Problem 6: Remove Nth Node from End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_nth_from_end(head, n):
    fast = slow = head

    for _ in range(n):
        fast = fast.next

    # edge case: [1]
    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return node.next


last = None
for i in range(5, 0, -1):
    node = ListNode(i)
    node.next = last
    last = node

# This will create the following input [1, [2, [3, [4, [5, None]]]]]
# Authored by NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/tests/test_problem06.py
remove_nth_from_end(last, 2)