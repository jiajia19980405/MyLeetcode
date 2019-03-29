class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        maxTail = []
        maxTail.append(nums[0])
        for i in range(1,len(nums)):
            maxTail.append(max(nums[i],maxTail[i-1]+nums[i]))
            m = max(maxTail[i],m)
        return m