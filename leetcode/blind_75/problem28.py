"""Problem 121: Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""


def max_profit(prices):
    """Authored by NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/problems/problem30.py
    
    This is a n-complexity algorithm which starts the comparison at the end of the list. We start by setting the max price and max profit to zero. 

    If current sell price is greater max price, max_price = price. We want to keep the highest possible selling price. 

    Else, we calculate the max profit by comparing the current max profit and the max_price - price. 
    """
    max_price = max_profit = 0
    for price in prices[::-1]:
        if price > max_price:
            max_price = price
        else:
            max_profit = max(max_profit, max_price - price)
    return max(max_profit, 0)


def max_profit_easy(prices):
    # Method: Peak and Valley
    # TC: O(n), SC: O(1)
    left = 0
    right = 1
    max_profit = 0
    
    while right < len(prices):
        if prices[left] < prices[right]:
            max_profit = max(max_profit, prices[right] - prices[left])
            right += 1
        else:
            left = right
            right += 1
    return max_profit

prices = [7,1,5,3,6,4]
assert max_profit_easy(prices) == 5