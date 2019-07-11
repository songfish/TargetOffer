# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]
        left = []
        right = []
        # 在二叉搜索树中左子树节点的值小于根节点的值
        for i in range(len(sequence)):
            if sequence[i] < root:
                left.append(sequence[i])
            else:
                break
        # 在二叉搜索树中右子树节点的值大于根节点的值
        for j in range(i, len(sequence)-1):
            if sequence[j] < root:
                return False
            else:
                right.append(sequence[j])
        # 判断左子树是不是二叉搜索树
        left_flag = True
        if i > 0:
            left_flag = self.VerifySquenceOfBST(left)
        # 判断右子树是不是二叉搜索树
        right_flag = True
        if i < len(sequence)-1:
            right_flag = self.VerifySquenceOfBST(right)
        return left_flag and right_flag


s = Solution()
# print(s.VerifySquenceOfBST([5,7,6,9,11,10,8]))
# print(s.VerifySquenceOfBST([4,8,6,12,16,14,10]))
print(s.VerifySquenceOfBST([7,4,6,5]))