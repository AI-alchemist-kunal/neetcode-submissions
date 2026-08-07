class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left = 0
        right = len(prices)-1
        maxprofit = 0

        while left < right:
            diff = prices[right]-prices[left]
            maxprofit = max(diff, maxprofit)
            left+=1
            right-=1

        if maxprofit > 0:
            return maxprofit
        else:
            return 0

        