# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.selfisSymmetrical(pRoot, pRoot)

    def selfisSymmetrical(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.selfisSymmetrical(pRoot1.left, pRoot2.right) and self.selfisSymmetrical(pRoot1.right, pRoot2.left)


pRoot1 = TreeNode(7)
pRoot2 = TreeNode(7)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(7)
pRoot5 = TreeNode(7)
pRoot6 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot3.left = pRoot6

s = Solution()
print(s.isSymmetrical(pRoot1))
