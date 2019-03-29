class Solution:
    def generate(self,l,r,string,li):
        if l==0 and r == 0:
            li.append(string)
        if l > 0:
            self.generate(l-1,r,string+'(',li)
        if l < r:
            self.generate(l,r-1,string+')',li)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        li = []
        self.generate(n,n,'',li)
        return li

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))