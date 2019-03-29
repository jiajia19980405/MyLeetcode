class Solution:
    def containsDuplicate(self, nums):
        hashmap = {}
        for num in nums :
            if num in hashmap:
                return True
            hashmap[num] = num
        
        return False