class Solution:
    def dfs(self,mark,i,j,m,n):
        print(i,j)
        if mark[i][j] >= 0:
            return mark[i][j]
        if i == n-1:
            mark[i][j] = self.dfs(mark,i,j+1,m,n)
        elif j == m-1:
            mark[i][j] = self.dfs(mark,i+1,j,m,n)
        else :
            mark[i][j] = self.dfs(mark,i,j+1,m,n) + self.dfs(mark,i+1,j,m,n)
        return mark[i][j]
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mark = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(-1)
            mark.append(temp)
        mark[n-1][m-1] = 1
        return self.dfs(mark,0,0,m,n)
if __name__ == '__main__':

    s = Solution()
    print(s.uniquePaths(12,23))