'''Problem 14: Spiral Matrix

https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''


def spiral_order(matrix):
  '''
  zip(*iterables) --> A zip object yielding tuples until an input is exhausted.

  >>> list(zip('abcdefg', range(3), range(4)))
  [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
  The zip object yields n-length tuples, where n is the number of iterables passed as positional arguments to zip(). 
  The i-th element in every tuple comes from the i-th iterable argument to zip(). 
  This continues until the shortest argument is exhausted.

  Unzipping zip:
  c, v = zip(*result)

  More fun solutions found here --> https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
  Ex: return matrix and [*matrix.pop(0)] + spiral_order([*zip(*matrix)][::-1]) // runtime of 16 ms, 99.91% 
  '''
  result = []
  while matrix:
    '''
    Technical Decisions:
    1) result.extend() is more expensive than += 
    https://stackoverflow.com/questions/3653298/concatenating-two-lists-difference-between-and-extend

    2) [*zip(*matrix)] unzips the zip values to a list.

    3) matrix.reverse() reverse in-place while matrix[::-1] (splicing) creates a new copy of the list. 

    Note: Once the matrix has been transposed by zi[], the datatype change from list -> tuple.
    But this is irrelevant because we add individual element as itself to result.
    '''
    result += matrix.pop(0)
    matrix = [*zip(*matrix)] # can also do list(zip(*matrix))
    matrix.reverse()
  return result


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
'''
// line 39
result = [1, 2, 3, 4]
matrix = [
  [5, 6, 7, 8],
  [9,10,11,12]

]
// line 40
matrix = [
  [9, 5],
  [10, 6],
  [11, 7],
  [12, 8]
]
//line 41
matrix = [
  [12, 8],
  [11, 7],
  [10, 6],
  [9, 5]
]
// line 39
result = [1, 2, 3, 4, 8, 12]

and so on...
'''

expected = [1,2,3,4,8,12,11,10,9,5,6,7]
actual = spiral_order(matrix)
print(expected == actual)