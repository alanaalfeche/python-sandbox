class Stack:    
    def __init__(self):
        self._array = []

    def is_empty(self):
        return len(self._array) == 0

    def push(self, x):
        return self._array.append(x)
    
    def pop(self):
        if self.is_empty(): 
            return 'underflow'
        else: 
            return self._array.pop()

stack = Stack()
print(stack.pop()) # throws underflow because it is empty
stack.push('1')
stack.push('2')
print(stack.pop()) # returns 2, last-in-first-out policy
