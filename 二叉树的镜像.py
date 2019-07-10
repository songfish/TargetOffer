# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left is not None:
            self.Mirror(root.left)
        if root.right is not None:
            self.Mirror(root.right)
        return root

    def Mirror2(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return root
        pTemp = root.left
        root.left = root.right
        root.right = pTemp
        self.Mirror2(root.left)
        self.Mirror2(root.right)
        return root


pRoot1 = TreeNode(8)
pRoot2 = TreeNode(6)
pRoot3 = TreeNode(10)
pRoot4 = TreeNode(5)
pRoot5 = TreeNode(7)
pRoot6 = TreeNode(9)
pRoot7 = TreeNode(11)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot3.left = pRoot6
pRoot3.right = pRoot7

s = Solution()
print(s.Mirror(pRoot1).val)
