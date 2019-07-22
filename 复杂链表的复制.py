# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        self.CloneNodes(pHead)   # 这里的pHead已经变成了1->1->3->3->5->5，因此进到ConnectSiblingNodes里面的pHead也是复制过的
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)

    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            # pCloned.random = pNode.random
            pNode.next = pCloned
            pNode = pCloned.next

    def ConnectSiblingNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    def ReconnectNodes(self, pHead):
        pNode = pHead
        # pClonedHead = None
        # pClonedNode = None
        # if pNode:
        #   pClonedNode = pNode.next
        #   pClonedHead = pClonedNode
        #   pNode.next = pClonedNode.next
        #   pNode = pNode.next
        pClonedNode = pNode.next
        pClonedHead = pClonedNode
        # pNode.next = pClonedNode.next
        pNode.next = pClonedHead.next
        pNode = pNode.next
        while pNode:
            # pNode.next = pClonedNode.next
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead

node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)