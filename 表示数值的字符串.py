# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        alist = [w.lower() for w in s]  # 目的是将E转为e
        if 'e' in alist:
            indexE = alist.index('e')  # 获取e的位置
            front = alist[:indexE]  # 将e前面的数字放在front中
            behind = alist[indexE+1:]  # 将e后面的数字放在behind中
            if '.' in behind or len(behind) == 0:  # 如果e后面中有'.',或者e后面没有东西， 那么就不是数值
                return False
            isFront = self.scanDigit(front)  # 判断e前面的是不是数值
            isBehind = self.scanDigit(behind)  # 判断e后面的是不是数值
            return isFront and isBehind
        else:
            return self.scanDigit(alist)  # 如果字符串中没有e，判断是不是数值

    def scanDigit(self, alist):
        allowVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', 'e', '.']
        dotNum = 0
        for i in range(len(alist)):
            if alist[i] not in allowVal:  # 如果不属于allowVal，就不是数值
                return False
            if alist[i] == '.':
                dotNum += 1
            if alist[i] in '+-' and i != 0:  # 如果是+-但是不在开头，就不是数值。
                return False
        if dotNum > 1:  # 如果小数点的数量大于1，那么就不是数值。
            return False
        return True

s = Solution()
result = s.isNumeric('123.45e+6')
print(result)