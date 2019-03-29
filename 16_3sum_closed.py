class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = None
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                l = i+1
                r = len(nums)-1
                while (l < r):
                    tar = nums[i] + nums[l] + nums[r]
                    if tar == target:
                        return nums[i]+nums[l]+nums[r]
                    if ans == None or abs(tar-target) < abs(ans - target):
                        ans = tar
                    if tar < target:
                        l += 1
                    else:
                        r -= 1
        return ans
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1,2,1,-4], 1))