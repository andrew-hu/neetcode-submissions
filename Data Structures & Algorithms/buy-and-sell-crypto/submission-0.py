class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxprofit = 0
        minimum = prices[0]
        while i < (len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            if prices[i] - minimum > maxprofit:
                maxprofit = prices[i] - minimum
            i = i + 1
        return maxprofit