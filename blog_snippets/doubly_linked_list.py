# Doubly Linked List
# L.head -> |/|9| | -> <- | |16| | -> <- | |4| | -> <- | |1|/|   

class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None # points to its successor
        self.prev = None # points to its predecessor
        
class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None # first element of a list
        self.tail = None
    
    def size(self):
        return self.length

    def insert(self, x):  # O(1)
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def delete(self, x): # O(n) because of search + delete
        node = self.head
        while node != None:
            if node.data == x:
                if node.prev != None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next != None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                self.length -=1
            node = node.next

    def search(self, x): # O(n)
        count = 1
        node = self.head
        while node != None and node.data != x:
            node = node.next
            count += 1
        return count


dll = LinkedList()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
print(dll.size()) # returns 5
print(dll.search(5)) # returns index=1
dll.delete(3)
print(dll.size()) # returns 4
print(dll.search(2)) # returns index=3
