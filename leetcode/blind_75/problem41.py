'''Problem 206: Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def reverse(head):
    prev = None
    
    while head:
        node = head
        head = head.next
        node.next = prev
        prev = node

    return prev


last = None
for i in range(5, 0, -1):
    node = ListNode(i)
    node.next = last
    last = node

answer = reverse(last)
for _ in range(5):
    print(answer.val)
    answer = answer.next