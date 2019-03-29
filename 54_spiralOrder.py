class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        row = len(matrix)
        if row == 0 :
            return ans
        col = len(matrix[0])
        mark = []
        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(True)
            mark.append(temp)
        i,j=0,0
        ans.append(matrix[i][j])
        mark[i][j] = False
        count = row * col -1
        while True:
            while j < col-1:
                if mark[i][j+1]:
                    j += 1
                    mark[i][j] = False
                    ans.append(matrix[i][j])
                    count -= 1
                else :
                    break
            while i < row-1:
                if mark[i+1][j]:
                    i += 1
                    mark[i][j] = False
                    ans.append(matrix[i][j])
                    count -= 1
                else :
                    break
            while j > 0 :
                if mark[i][j-1]:
                    j -= 1
                    mark[i][j] = False
                    ans.append(matrix[i][j])
                    count -= 1
                else :
                    break
            while i > 0 :
                if mark[i-1][j]:
                    i -= 1
                    mark[i][j] = False
                    ans.append(matrix[i][j])
                    count -= 1
                else :
                    break
            if count == 0:
                break
        return ans
if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))