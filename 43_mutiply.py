class Solution:
    def singleMutiply(self, ch, num):
        ans = ''
        carry = 0
        n = int(ch)
        for i in range(1,len(num)+1):
            temp = int(num[-i])*n
            res = carry + temp % 10
            carry = res // 10 + temp // 10
            ans = str(res%10) + ans
        if carry != 0:
            ans = str(carry) + ans
        return ans
    def add(self, addend, addenor, shift):
        addenor = addenor + shift * '0'
        carry = 0
        ans = ''
        for i in range(1,len(addend)+1):
            temp = int(addend[-i]) + int(addenor[-i])
            res = carry + temp % 10
            carry = res // 10 + temp // 10
            ans = str(res%10) + ans
        addenor = addenor[:-len(addend)]
        if len(addenor) > 0 :
            for i in range(1,len(addenor)+1):
                temp = int(addenor[-i])
                res = carry + temp % 10
                carry = res // 10 + temp // 10
                ans = str(res%10) + ans
        if carry != 0:
            ans = str(carry) + ans
        return ans


    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = '0'
        shift = 0
        for i in range(1,len(num1)+1):
            temp = self.singleMutiply(num1[-i],num2)
            ans = self.add(ans, temp, shift)
            shift += 1
        while len(ans) > 1 and ans[0] == '0':
            ans = ans[1:]
        return ans 
if __name__ == "__main__":
    s = Solution()
    print(s.multiply('9133','0'))