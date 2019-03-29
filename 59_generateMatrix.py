class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            matrix.append(temp)
        end = n * n
        curr = 1
        matrix[0][0] = curr
        curr += 1
        i, j = 0,0
        while curr <= end :
            while j < n-1 :
                if matrix[i][j+1] == 0:
                    j += 1
                    matrix[i][j] = curr
                    curr += 1
                else :
                    break
            while i < n-1 :
                if matrix[i+1][j] == 0:
                    i += 1
                    matrix[i][j] = curr
                    curr += 1
                else :
                    break
            while j > 0 :
                if matrix[i][j-1] == 0:
                    j -= 1
                    matrix[i][j] = curr
                    curr += 1
                else :
                    break
            while i > 0 :
                if matrix[i-1][j] == 0:
                    i -= 1
                    matrix[i][j] = curr
                    curr += 1
                else :
                    break
        return matrix