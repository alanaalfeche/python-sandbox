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