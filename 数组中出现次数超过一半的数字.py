# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        save_frequence = dict()
        for data in numbers:
            if data not in save_frequence:
                save_frequence[data] = 1
            else:
                save_frequence[data] += 1
        length = len(numbers) / 2
        for i in save_frequence.values():
            if i > length:
                result = list(save_frequence.keys())[list(save_frequence.values()).index(i)]
                return result
        return 0


s = Solution()
print(s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))