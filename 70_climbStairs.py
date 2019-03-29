class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a,b = 1,2
        ans = 0
        for i in range(2,n):
            ans = a + b
            a = b
            b = ans
        return ans