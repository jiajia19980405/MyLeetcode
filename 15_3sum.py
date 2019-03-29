class Solution:
    #时间复杂度O（n^2)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        #step 1 sort nums

        nums.sort() #此处时间复杂度O(nlogn)

        #step 2 遍历i, 将三数之和转化为2数之和

        for i in range(len(nums)): 
            if i == 0 or nums[i]>nums[i-1]: #用于对i去重
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        ans.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return ans

if __name__ == "__main__":
    
    test = [-1,0,1,2,-1,-4]
    sol = Solution()
    print (sol.threeSum(test))