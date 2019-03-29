class Solution:
    def recallway(self, nums, lists, lis):
        if len(nums) == 0 :
            lists.append(lis)
        else :
            for i in range(len(nums)) :
                temp = []
                for j in range(len(nums)):
                    if j != i :
                        temp.append(nums[j])
                self.recallway(temp,lists,lis + [nums[i]])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.recallway(nums,ans,[])
        return ans
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))