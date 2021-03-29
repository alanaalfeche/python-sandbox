'''Context Managers
Context Managers allow you to allocate and release resources precisely when you want to. 
This is primarily useful for two related operations which you'd like to execute as a pair. 

At the very least a context manager has an __enter__ and __exit___ method defined.

- When the "with" statement is executed, the method __enter__() is called.
- The returned value is assigned to the variable defined by "as" which is "indent" in this example.
- The variable "indent" is only availabe within the the block below the "with" statement. 
- Once the block ends, the variable "indent" goes out of scope, triggering __exit__() which clean up the resources.
'''

class Indenter:
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('   ' * self.level + text)


with Indenter() as indent:
    ''' prints: 
    hi
        hola
            bonjour
    hey
    '''
    indent.print('hi')
    with indent:
        indent.print('hola')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
