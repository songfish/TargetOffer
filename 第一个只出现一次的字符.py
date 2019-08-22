# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        result = {}
        for i in s:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        for index, v in enumerate(s):
            if result[v] == 1:
                return index
        return -1


s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))