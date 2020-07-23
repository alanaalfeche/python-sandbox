from heapq import heappush, heappop


def heapsort(iterable):
    # https://docs.python.org/2/library/heapq.html
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))