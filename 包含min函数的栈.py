# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            tmp = self.min()
            self.minStack.append(tmp)

    def pop(self):
        # write code here
        if self.stack == [] or self.minStack == []:
            return None  # 更严谨一点
        self.stack.pop()  # 这个pop不是这个pop方法，是列表的pop方法而已
        self.minStack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]


S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())