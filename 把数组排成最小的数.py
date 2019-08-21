# -*- coding:utf-8 -*-
from functools import cmp_to_key

class Solution:
    def comp(self,x,y):
        s = str(x) + str(y)
        t = str(y) + str(x)
        if s > t:
            return 1
        elif s < t:
            return -1  # 就表示 x < y,x放在y前面
        else:
            return 0

    def PrintMinNumber(self, numbers):
        # write code here
        result = sorted(numbers, key=cmp_to_key(self.comp))
        return ''.join(str(x) for x in result)


s = Solution()
print(s.PrintMinNumber([3, 32, 321]))