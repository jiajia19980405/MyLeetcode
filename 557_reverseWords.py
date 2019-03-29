class Solution:
    def reverseWords(self, s):
        words = s.split(' ')
        ans = ''
        for j in range(len(words)):
            word = words[j]
            newWord = ''
            for i in range(len(word)-1,-1,-1):
                newWord += word[i]
            if j < len(words) - 1 :
                ans += newWord + ' '
            else:
                ans += newWord
        return ans