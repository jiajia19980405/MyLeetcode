class Solution:
    def majorityElement(self, nums):
        count = 0
        ans = nums[0]
        for i in range(0,len(nums)):
            if count == 0:
                ans = nums[i]
            if ans == nums[i] :
                count += 1
            else:
                count -= 1
        return ans