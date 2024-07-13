#Best Time to Buy and Sell Stock II

#When we have profit, sell the current stock and
# buy the same stock to have profit
# When the stock are low, it's time to buy it, update new time's buy 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        total = 0
        profit = 0
        for x in prices:
            if x < buy:
                buy = x
            else:
                profit = x - buy
                total += profit
                buy = x
            
        return total
        