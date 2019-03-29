class Solution:
    def projectionArea(self, grid):
        front = {}
        top = 0
        left = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    top += 1
                if j not in front :
                    front[j] = grid[i][j]
                else :
                    front[j] = max(front[j],grid[i][j])
                if i not in left :
                    left[i] = grid[i][j]
                else :
                    left[i] = max(left[i],grid[i][j])

        summ = 0
        for num in front.values() :
            summ += num
        for num in left.values() :
            summ += num
        return summ + top
if __name__ == '__main__':
    s = Solution()
    print(s.projectionArea([[2]]))