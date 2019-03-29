class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        else :
            
            for i in range(len(haystack)):
                if needle[0] == haystack[i]:
                    flag = True
                    for j in range(1,len(needle)):
                        try:
                            if haystack[i+j] != needle[j]:
                                flag = False
                                break
                        except:
                            return -1
                    if flag :
                        return i
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi","issip"))