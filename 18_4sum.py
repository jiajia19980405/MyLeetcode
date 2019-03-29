class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                newtarget = target - nums[i]
                for j in range(i+1,len(nums)):
                    if j == i+1 or nums[j] > nums[j-1]:
                        l, r = j+1, len(nums)-1
                        while l < r:
                            if nums[j] + nums[l] + nums[r] == newtarget:
                                ans.append([nums[i],nums[j],nums[l],nums[r]])
                                while l < r and nums[l] == nums[l+1]:
                                    l += 1
                                while l < r and nums[r] == nums[r-1]:
                                    r -= 1
                                l += 1
                                r -= 1
                            elif nums[j] + nums[l] + nums[r] < newtarget:
                                l += 1
                            else :
                                r -= 1
        return ans
if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([0,0,0,0], 0))
                            