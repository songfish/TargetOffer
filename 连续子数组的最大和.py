# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        cur_sum = 0
        great_sum = array[0]  # 这个原来写的0，对于样例[-2,-8,-1,-5,-9]应该输出-1，结果输出0
        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]
            else:
                cur_sum = cur_sum + array[i]
            if cur_sum > great_sum:
                great_sum = cur_sum
        return great_sum


s = Solution()
print(s.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))
