class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length=len(prices)
        for i in range(length):
            for j in range(i+1, length):
                localProfit = prices[j] - prices[i]
                if localProfit > profit:
                    profit=localProfit
        
        
        return profit