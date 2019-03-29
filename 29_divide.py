class Solution:
    
    def negative(self, n):
        return ~n+1

    def positive(self, n):
        t = n >> 31
        return (n + t) ^ t

    def negpos(self, sign, n):
        return self.positive(n) if sign else self.negative(n)

    def divide(self, dividend, divisor):
        
        sign = dividend >> 31 == divisor >> 31
        dividend = self.positive(dividend)
        divisor = self.positive(divisor)

        cnt, minus = 0, divisor
        while dividend >= minus:
            minus <<= 1
            cnt += 1

        if cnt == 0:
            return 0

        r = self.negpos(sign, 2**(cnt-1) +
                        self.divide(dividend-(minus >> 1), divisor))

        if r < -2**31 or r > 2**31 - 1:
            return 2**31 - 1

        return r

