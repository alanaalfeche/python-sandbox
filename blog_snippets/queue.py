class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, x):
        node = Node(x)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail 
            self.tail = node
        self.length += 1

    def deque(self):
        item = self.head.item
        self.head = self.head.next
        self.length -= 1
        return item

    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.deque()) # returns 1, first-in-first-out policy
