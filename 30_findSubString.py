class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        sizes = len(words)
        if sizes == 0:
            return []
        length = len(words[0])
        ans = []
        
        for i in range(len(s)-sizes*length+1):
            firstWord = s[i:i+length]
            marks = words[:]
            flag = False
            for k in range(sizes):
                if marks[k] == firstWord:
                    marks[k] = False
                    flag = True
                    break
            if flag :
                for j in range(i+length,i+length*sizes,length):
                    flag = False
                    nextWord = s[j:j+length]
                    for k in range(sizes):
                        if marks[k] == nextWord:
                            marks[k] = False
                            flag = True
                            break
                    if not flag :
                        break
            if flag:
                ans.append(i)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))