class Solution:

    def findBegin(self,nums,begin,end):
        if begin >= end or nums[begin] < nums[end-1]:
            return -1
        else :
            med = (begin + end) // 2
            if med == 0 :
                return 0
            elif nums[med] < nums[med-1] :
                return med
            elif med != len(nums)-1 and nums[med] > nums[med+1]:
                return med+1
            else :
                return max(self.findBegin(nums,begin,med),self.findBegin(nums,med+1,end))
    def binFind(self,nums,begin,end,target):
        if begin >= end :
            return -1
        med = (begin + end) // 2
        if nums[med] == target:
            return med
        elif nums[med] > target :
            return self.binFind(nums, begin, med, target)
        else :
            return self.binFind(nums, med+1, end, target)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #处理特殊情况
        if len(nums) == 0:
            return -1
        #第一步 寻找起点
        begin = self.findBegin(nums,0,len(nums))
        #第二步 寻找target
        if target > nums[len(nums)-1]:
            return self.binFind(nums,0,begin,target)
        else :
            return self.binFind(nums,begin,len(nums),target)
if __name__ == '__main__':
    s = Solution()
    print(s.search([2,3,4,5,6,7,8,9,1],3))