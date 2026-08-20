class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        left = 0
        maxprofit = 0

        for right in range(1, len(prices)):
            
            # If selling today gives profit
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            
            # Found a cheaper buying price
            else:
                left = right


        return maxprofit