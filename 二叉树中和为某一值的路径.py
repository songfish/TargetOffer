# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if not root.left and not root.right:  # 如果是叶子节点
            if expectNumber == root.val:
                return [[root.val]]
            else:
                return []
        stack = []
        leftStack = self.FindPath(root.left, expectNumber-root.val)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
        rightStack = self.FindPath(root.right, expectNumber-root.val)
        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return sorted(stack, key=len, reverse=True)  # 为了使得list长度长的在前面
        # return stack

# example1
# pNode1 = TreeNode(10)
# pNode2 = TreeNode(5)
# pNode3 = TreeNode(12)
# pNode4 = TreeNode(4)
# pNode5 = TreeNode(7)
# pNode1.left = pNode2
# pNode1.right = pNode3
# pNode2.left = pNode4
# pNode2.right = pNode5


# example2
pNode1 = TreeNode(10)
pNode2 = TreeNode(12)
pNode3 = TreeNode(5)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)
pNode1.left = pNode2
pNode1.right = pNode3
pNode3.left = pNode4
pNode3.right = pNode5
s = Solution()
print(s.FindPath(pNode1, 22))
