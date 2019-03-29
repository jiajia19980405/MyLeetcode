class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums)
        while i < length :
            if i != 0 and nums[i] == nums[i-1]:
                del nums[i]
                length -= 1
            else:
                i += 1