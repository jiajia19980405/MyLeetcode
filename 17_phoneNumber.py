class Solution:
    numbers = {'2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'}
    def letterCombinations(self, digits):
        
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        for digit in digits:
            letters = self.numbers[digit]

            if ans == []:

                ans = [letter for letter in letters]

            else:
                temp = ans[:]
                ans = []
                for letter in letters:
                    ans += [temp[i] + letter for i in range(len(temp))]
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations('23'))
                            
