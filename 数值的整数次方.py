# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            result = 1
        if exponent < 0:
            result = 1 / base
            for i in range(abs(exponent)-1):
                result = result / base
        if exponent > 0:
            result = base
            for i in range(exponent-1):
                result = result * base
        return result

    def Power1(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1 / base
        result = self.Power1(base, exponent >> 1)
        result *= result
        if (exponent & 0x1) == 1:  # 判断是不是奇数，是的话还得再乘一个基底
            result *= base
        return result


s = Solution()
print(s.Power1(2, -3))

