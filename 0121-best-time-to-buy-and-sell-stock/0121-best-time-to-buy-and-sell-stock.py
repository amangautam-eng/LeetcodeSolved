class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profit,buy=0,float('inf')

        for x in prices:

            if x<buy:
                buy=x
            
            profit=max(profit,x-buy)

        return profit