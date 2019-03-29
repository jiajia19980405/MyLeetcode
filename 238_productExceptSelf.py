class Solution:
    def productExceptSelf(self, nums):
        mark1 = [0 for num in nums]
        mark2 = [0 for num in nums]
        ans = [0 for num in nums]
        for i in range(len(nums)):
            if i == 0 :
                mark1[i] = nums[i]
            else :
                mark1[i] = nums[i] * mark1[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                mark2[i] = nums[i]
            else :
                mark2[i] = nums[i] * mark2[i+1]
        for i in range(len(nums)):
            if i == 0 :
                ans[i] = mark2[1]
            elif i == len(nums)-1:
                ans[i] = mark1[len(nums)-2]

            else:
                ans [i] = mark1[i-1] * mark2[i+1]
        return ans 