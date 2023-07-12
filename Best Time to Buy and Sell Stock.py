class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        minPrice = float("inf") #highest positive integer value
        for price in prices:
            minPrice = min(minPrice,price)
            profit = max(profit,price-minPrice)
        return profit