class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        
        # Loop through prices starting from the second day
        for i in range(1, len(prices)):
            # If the price today is higher than yesterday, take the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit
