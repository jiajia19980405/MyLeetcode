class Solution:
    maxRes = 0x8000000
    def findMaxres(self, nums, begin, end):
        if len(nums) == 1 :
            if nums[0] >self.maxRes :
                maxRes = nums[0]
            return [nums[0],nums[0],[begin,end],[begin,end]]
        else :
            med = (begin + end) // 2
            rres = self.findMaxres(nums, begin, med)
            lres = self.findMaxres(nums, med+1, end)
            self.maxRes = max(self.maxRes, rres[0]+lres[1])
            

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        