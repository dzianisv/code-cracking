"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        prev_price = prices[0]
        total_profit = 0
        
        for price in prices[1:]:
            if prev_price < price:
                profit = price - prev_price
                total_profit += profit
                
            prev_price = price
        
        return total_profit