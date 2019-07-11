# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = []
        stack0 = [root]
        stack1 = []
        stack = [stack0, stack1]
        current = 0
        next = 1
        while stack[current] or stack[next]:
            node = stack[current].pop()
            result.append(node.val)
            if current == 0:
                if node.left:
                    stack[next].append(node.left)
                if node.right:
                    stack[next].append(node.right)
            else:
                if node.right:
                    stack[next].append(node.right)
                if node.left:
                    stack[next].append(node.left)
            if not stack[current]:
                current = 1 - current
                next = 1 - next
        return result


pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)
pNode8 = TreeNode(8)
pNode9 = TreeNode(9)
pNode10 = TreeNode(10)
pNode11 = TreeNode(11)
pNode12 = TreeNode(12)
pNode13 = TreeNode(13)
pNode14 = TreeNode(14)
pNode15 = TreeNode(15)
pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7
pNode4.left = pNode8
pNode4.right = pNode9
pNode5.left = pNode10
pNode5.right = pNode11
pNode6.left = pNode12
pNode6.right = pNode13
pNode7.left = pNode14
pNode7.right = pNode15
s = Solution()
print(s.PrintFromTopToBottom(pNode1))
