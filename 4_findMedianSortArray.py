class Solution:

    length1 = 0
    length2 = 0

    def numsLower(self, nums, target, begin, end):
        mid = (begin + end)//2
        if len(nums) == 0 :
            return 0
        if mid == 0 and nums[mid] >= target:
            return 0
        elif mid == len(nums)-1 and nums[mid] < target:
            return mid+1
        elif nums[mid] <= target and nums[mid+1] > target:
            return mid+1
        elif nums[mid] >= target:
            return self.numsLower(nums,target,begin,mid)
        else:
            return self.numsLower(nums,target,mid+1,end)
    def nextNum(self, nums,target,begin,end):
        if len(nums) == 0 :
            return 0x7fffffff
        mid = (begin + end)//2
        if mid == 0 and nums[mid] >= target:
            return nums[0]
        elif mid == len(nums)-1 and nums[mid] < target:
            return 0x7fffffff
        elif nums[mid] <= target and nums[mid+1] > target:
            return nums[mid+1]
        elif nums[mid] >= target:
            return self.nextNum(nums,target,begin,mid)
        else:
            return self.nextNum(nums,target,mid+1,end)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #避免重复运算
        self.length1 = len(nums1)
        self.length2 = len(nums2)

        if (self.length1 + self.length2) % 2 == 1:
            #奇数情况
            begin = 0
            end = self.length1
            while begin < end :
                mid = (end + begin) // 2
                a = mid
                b = self.numsLower(nums2,nums1[mid],0,self.length2)
                if a + b == (self.length1 + self.length2) // 2:
                    return float(nums1[mid])
                elif a + b < (self.length1 + self.length2) // 2:
                    begin = mid + 1
                else :
                    end = mid
            begin = 0
            end = self.length2
            while begin < end :
                mid = (end + begin) // 2
                a = mid
                b = self.numsLower(nums1,nums2[mid],0,self.length1)
                if a + b == (self.length1 + self.length2) // 2:
                    return float(nums2[mid])
                elif a + b < (self.length1 + self.length2) // 2:
                    begin = mid + 1
                else :
                    end = mid
        else :
            #偶数情况
            begin = 0
            end = self.length1
            while begin < end :
                mid = (end + begin) // 2
                a = mid
                b = self.numsLower(nums2,nums1[mid],0,self.length2)
                if a + b == (self.length1 + self.length2) // 2 - 1:
                    if mid == self.length1-1:
                        nextn = self.nextNum(nums2,nums1[mid],0,self.length2)
                    else :
                        nextn = min(nums1[mid+1], self.nextNum(nums2,nums1[mid],0,self.length2))

                    return float((nextn + nums1[mid])/2)
                elif a + b < (self.length1 + self.length2) // 2 - 1:
                    begin = mid + 1
                else :
                    end = mid
            begin = 0
            end = self.length2
            while begin < end :
                mid = (end + begin) // 2
                a = mid
                b = self.numsLower(nums1,nums2[mid],0,self.length1)
                if a + b == (self.length1 + self.length2) // 2 - 1:
                    if mid == self.length2-1:
                        nextn = self.nextNum(nums1,nums2[mid],0,self.length1)
                    else :
                        nextn = min(nums2[mid+1], self.nextNum(nums1,nums2[mid],0,self.length1))

                    return float((nextn + nums2[mid])/2)
                elif a + b < (self.length1 + self.length2) // 2 - 1:
                    begin = mid + 1
                else :
                    end = mid
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,2],[1,2]))