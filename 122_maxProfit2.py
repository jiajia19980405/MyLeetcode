class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        maxP = 0
        ans = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i] - buy
            if profit >= maxP:
                maxP = profit
            else:
                ans += maxP
                buy = prices[i]
                maxP = 0
        return ans + maxP

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))