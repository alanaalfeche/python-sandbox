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
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def delete(self, x): # O(n) because of search + delete
        curNode = self.head
        while curNode != None:
            if curNode.data == x:
                if curNode.prev != None:
                    curNode.prev.next = curNode.next
                else:
                    self.head = curNode.next
                if curNode.next != None:
                    curNode.next.prev = curNode.prev
                else:
                    self.tail = curNode.prev
                self.length -=1
            curNode = curNode.next

    def search(self, x): # O(n)
        count = 1
        curNode = self.head
        while curNode != None and curNode.data != x:
            curNode = curNode.next
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
