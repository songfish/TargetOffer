# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pReversedHead = None
        pNode = pHead
        pPrev = None
        while(pNode != None):
            pNext = pNode.next
            if(pNext == None):
                pReversedHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
print(s.ReverseList(node1).val)