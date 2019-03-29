class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i,j=0,0
        end = m-1
        while j<n:
            while nums1[i] <= nums2[j] and i <= end:
                i+= 1
            if i > end:
                while j < n:
                    nums1[i] = nums2[j]
                    i+= 1
                    j+= 1
            else:
                begin = j
                while j < n and nums1[i] > nums2[j]:
                    j += 1
                shift = j-begin
                k = end
                end = end + shift
                while k >= i:
                    nums1[k+shift] = nums1[k]
                    k -= 1
                for k in range(i,i+shift):
                    nums1[k] = nums2[begin]
                    begin += 1
                    i += 1
if __name__ == '__main__':
    s = Solution()
    a = [2,0]
    b = [1]
    s.merge(a,1,b,1)
    print(a)
