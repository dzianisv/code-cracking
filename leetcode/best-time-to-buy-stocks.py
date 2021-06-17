# Naive solution
# class Solution(object):
#     def maxProfit(self, prices):
#         m = 0
#         for i in  range(0, len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 m = max(m ,prices[j]-prices[i])
#         return m
        
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        maxProfit = 0
        minPrice = prices[0]
        for price in prices[1:]:
            profit = price - minPrice
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, profit)
            
        return maxProfit