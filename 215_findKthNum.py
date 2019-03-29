class Solution:
    def findKthLargest(self, nums, k):
        for i in range(len(nums)//2-1,-1,-1):
            j = i
            #sink
            while (j <= len(nums)//2-1):
                ls, rs = 2*j+1, 2*j+2
                if rs >= len(nums):
                    if nums[j] >= nums[ls]:
                        break
                    else:
                        nums[j],nums[ls] = nums[ls], nums[j]
                        break
                if nums[j] >= nums[ls] and nums[j] >= nums[rs]:
                    break
                else :
                    temp = 0
                    if nums [ls] > nums[rs] :
                        temp = ls
                    else:
                        temp = rs
                    nums[j], nums[temp] = nums[temp], nums[j]
                    j = temp
        l = len(nums)-1
        for i in range(0,k-1):
            nums[0], nums[l] = nums[l], nums[0]
            j = 0
            #sink
            while (j <= l//2-1):
                ls, rs = 2*j+1, 2*j+2
                if rs >= l:
                    if nums[j] >= nums[ls]:
                        break
                    else:
                        nums[j],nums[ls] = nums[ls], nums[j]
                        break
                if nums[j] >= nums[ls] and nums[j] >= nums[rs]:
                    break
                else :
                    temp = 0
                    if nums [ls] > nums[rs] :
                        temp = ls
                    else:
                        temp = rs
                    nums[j], nums[temp] = nums[temp], nums[j]
                    j = temp
            l -= 1
        return nums[0]

if __name__ == '__main__':
    s = Solution()
    print (s.findKthLargest([2,1],2))