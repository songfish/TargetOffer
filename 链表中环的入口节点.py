# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        meetingNode = self.MeetingNode(pHead)
        if meetingNode is None:
            return None
        pNode1 = meetingNode
        count = 1
        while pNode1.next != meetingNode:
            pNode1 = pNode1.next
            count += 1
        pNode1 = pHead
        for i in range(count):
            pNode1 = pNode1.next
        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1

    def MeetingNode(self, pHead):
        if pHead == None:
            return None
        pFast = pHead
        pSlow = pHead.next
        while pSlow is not None and pFast is not None:
            if pSlow == pFast:
                return pFast
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast is not None:
                pFast = pFast.next
        return None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3
S = Solution()
print(S.EntryNodeOfLoop(node1).val)
