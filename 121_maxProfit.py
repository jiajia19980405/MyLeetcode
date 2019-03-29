class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        maxP = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i] - buy
            if profit >= 0 :
                maxP = max(maxP, profit)
            else:
                buy = prices[i]
        return maxP