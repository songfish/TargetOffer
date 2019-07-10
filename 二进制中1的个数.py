# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xFFFFFFFF
        while(n):
            count += 1
            n = (n - 1) & n
        return count


s = Solution()
result = s.NumberOf1(-2)
print(result)



