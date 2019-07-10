# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None:
            return
        preHead = None
        pNode = pHead
        while pNode is not None:  # 如果节点不为空，进入循环
            needDelete = False  # 一个标志
            nextNode = pNode.next  # 下个节点
            if nextNode is not None and nextNode.val == pNode.val:  # 如果下个节点不为空，且下个节点的值等于目前这个节点的值，标志为True
                needDelete = True
            if not needDelete:  # 如果标志为False，那么preHead为目前的节点，目前的节点为下一个节点。意思是指到下一个去了。
                preHead = pNode
                pNode = pNode.next
            else:  # 如果标志位True，即下个节点的值等于目前这个节点的值，那么nodeVal是现在目前节点的值，pToBeDel为目前的节点
                nodeVal = pNode.val
                pToBeDel = pNode
                while pToBeDel is not None and pToBeDel.val == nodeVal:  # 如果目前的节点不为空而且pToBeDel的值为目前节点的值，那么pToBeDel为他的下个节点
                    pToBeDel = pToBeDel.next
                if preHead is None:  # 如果preHead为None那么pHead和pNode为pToBeDel
                    pHead = pToBeDel  # 要返回的值
                    pNode = pToBeDel
                    continue
                else:  # 否则 preHead的下个节点为pToBeDel
                    preHead.next = pToBeDel
                pNode = preHead
        return pHead


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.deleteDuplication(node1).next.next.val)