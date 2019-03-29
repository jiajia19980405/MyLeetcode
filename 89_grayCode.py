class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(2**n):
            ans.append(i^(i//2))
        return ans
