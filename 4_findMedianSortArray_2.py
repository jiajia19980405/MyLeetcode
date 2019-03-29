class Solution:
    def judge(self, nums, low, res):
        '''
        return 0 表示正好有low个比res小
        return 1 表示low需要大一点
        return -1 表示low需要小一点
        '''
        if low < 0 :
            return -1
        elif low == 0 :
            if len(nums) == 0 :
                return 0
            else :
                if nums[0] >= res:
                    return 0
                else :
                    return -1
        
        elif low > len(nums):
            return 1

        elif low == len(nums):
            if res >= nums[-1]:
                return 0
            else :
                return 1
        else :
            if res >= nums[low-1] and res <= nums[low]:
                return 0
            elif res > nums[low]:
                return -1
            else :
                return 1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #step1 找到nums1中的某个值
        length1 = len(nums1)
        length2 = len(nums2)
        if (length1 + length2) % 2 == 1:
            s = (length1 + length2) // 2
            begin = 0
            end = length1
            while begin < end:
                med = (end + begin) // 2
                low1 = med
                res = nums1[med]
                low2 = s - med
                judgeRes = self.judge(nums2, low2, res)
                if judgeRes == 0 :
                    return float(res)
                elif judgeRes > 0 :
                    begin = med+1
                else:
                    end = med
            begin = 0
            end = length2
            while begin < end:
                med = (end + begin) // 2
                low2 = med
                res = nums2[med]
                low1 = s - med
                judgeRes = self.judge(nums1, low1, res)
                if judgeRes == 0 :
                    return float(res)
                elif judgeRes > 0 :
                    begin = med+1
                else:
                    end = med
            
        else :
            s = (length1 + length2) // 2 - 1
            begin = 0
            end = length1
            while begin < end:
                med = (end + begin) // 2
                low1 = med
                res = nums1[med]
                low2 = s - med
                judgeRes = self.judge(nums2, low2, res)
                if judgeRes == 0 :
                    if med + 1 >= length1:
                        smallestBigger = nums2[low2]
                    elif low2 >= length2 :
                        smallestBigger = nums1[med + 1]
                    else :
                        smallestBigger = min(nums1[med+1],nums2[low2])
                    return float((res + smallestBigger) / 2)
                elif judgeRes > 0 :
                    begin = med+1
                else:
                    end = med
            
            s = (length1 + length2) // 2 - 1
            begin = 0
            end = length2
            while begin < end:
                med = (end + begin) // 2
                low2 = med
                res = nums2[med]
                low1 = s - med
                judgeRes = self.judge(nums1, low1, res)
                if judgeRes == 0 :
                    if med + 1 >= length2:
                        smallestBigger = nums1[low1]
                    elif low1 >= length1 :
                        smallestBigger = nums2[med + 1]
                    else :
                        smallestBigger = min(nums2[med+1],nums1[low1])
                    return float((res + smallestBigger) / 2)
                elif judgeRes > 0 :
                    begin = med+1
                else:
                    end = med
                
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,2],[-1,3]))
            
