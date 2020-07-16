class MinHeap():
    """
    For every node x with parent p, they key in p must always be less than or equal to the key in x. 
    https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
    """
    def __init__(self):
        # implementing entire binary heap as a single list
        self.heap_list = [0]
        self.curr_size = 0

    def size(self):
        return self.curr_size

    def min_child(self, i):
        if i * 2 + 1 > self.curr_size:
            return i * 2
        else: 
            if self.heap_list[i * 2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_up(self, i):
        # keep heap order by swapping child - parent if it violates the property
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                 self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def perc_down(self, i):
        # swap root with its smallest child less than the root
        while (i * 2) <= self.curr_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def insert(self, k):
        """
        easiest and efficient way to add is to appent item to the end of the list
        benefit: it guarantees complete tree property
        problem: might violate the heap structure property
        solution: perc_up
        """
        self.heap_list.append(k)
        self.curr_size += 1
        self.perc_up(self.curr_size)

    def del_min(self):
        """
        smallest will always be at the root
        making last item as root maintains heap structure 
        problem: violate the heap order 
        solution: perc_down
        """
        val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        self.heap_list.pop()
        self.perc_down(1)

        return val
        
    def build_heap(self, alist):
        i = len(alist) // 2
        self.curr_size = len(alist)
        self.heap_list = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i -= 1

mh = MinHeap()
mh.build_heap([9,5,6,2,3])
print(mh.del_min())
print(mh.del_min())
print(mh.del_min())
print(mh.del_min())
print(mh.del_min())