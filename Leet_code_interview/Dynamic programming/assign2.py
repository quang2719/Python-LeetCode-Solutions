#Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # a[] - if to day sell stock, what is max benefit ?
        a = [0 for _ in range(len(prices))]
        if len(prices)==1: return 0
        for i in range(1,len(prices)):
            if prices[i] <= prices[i-1]:
                a[i] = a[i-1] - (prices[i-1]-prices[i])
                a[i] = max(0,a[i])
            else:
                a[i] = a[i-1] + (prices[i]-prices[i-1])
        return max(a)
        