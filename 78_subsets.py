class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        length = len(nums)
        for i in range(2**length):
            temp = []
            t = i
            for j in range(length):
                if t % 2 == 1:
                    temp.append(nums[j])
                t = t // 2
            ans.append(temp)
        return ans