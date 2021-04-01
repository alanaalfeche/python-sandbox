"""Logic 2. Make Bricks

We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 

Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. 
"""
def make_bricks(small, big, goal): # times out
    available_bricks = [1]*small + [5]*big
    curr_sum = 0

    sums = {}
    sums[0] = 1

    for brick in available_bricks:
        curr_sum += brick
        if (curr_sum - goal) in sums:
            return True
            
        sums[curr_sum] = sums.get(curr_sum,0) + 1

    return False


def make_bricks_without_for_loop(small, big, goal):
    big_needed = min(big, goal // 5)
    return goal - (big_needed * 5) <= small


expected = True
actual = make_bricks_without_for_loop(20, 0, 19)
assert actual is expected


"""String 2. Count Code
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.
"""
def count_code(str):
  i, count = 0, 0
  while i < len(str)-3:
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
      count += 1
      i = i+3
    else:
      i += 1
      
  return count

expected = 2
actual = count_code('codexxcode')
assert actual is expected

"""List 2. Sum 67
Return the sum of the numbers in the array, except ignore sections of numbers
starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 

Return 0 for no numbers.
"""
def sum67(nums):
    i, total = 0, 0
    skip = False

    while i < len(nums):
        if nums[i] == 6:
            skip = True

        if not skip:
            total += nums[i]

        if nums[i] == 7:
            skip = False

        i += 1

    return total


expected = 5
actual = sum67([1, 2, 2, 6, 99, 99, 7])
assert actual is expected


"""List 2. Centered Average
Return the "centered" average of an array of ints,
which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array. 

If there are multiple copies of the smallest value, ignore just one copy,
and likewise for the largest value. Use int division to produce the final average.

You may assume that the array is length 3 or more.
"""
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(alist):
    if len(alist) < 2:
        return alist
    else:
        mid = len(alist) // 2
        left = merge_sort(alist[:mid])
        right = merge_sort(alist[mid:])
        return merge(left, right)

def centered_average(nums):
    return sum(merge_sort(nums)[1:-1])/(len(nums)-2)

expected = 3
actual = centered_average([1, 2, 3, 4, 100]) 
assert int(actual) is expected