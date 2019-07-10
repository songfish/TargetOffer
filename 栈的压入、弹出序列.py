# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            if stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        while len(popV) > 0 and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        else:
            return True

    def IsPopOrder2(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(popV) > 0 and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        else:
            return True



s = Solution()
# print(s.IsPopOrder([1,2,3,4,5],[4,3,5,1,2]))
print(s.IsPopOrder2([1,2,3,4,5],[4,5,3,2,1]))
# print(s.IsPopOrder([1,2,3,4,5],[3,5,4,1,2]))