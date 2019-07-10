# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None

        pAHead = head
        pBehind = None

        for i in range(k - 1):
            if pAHead.next != None:
                pAHead = pAHead.next
            else:
                return None
        pBehind = head
        while pAHead.next != None:
            pAHead = pAHead.next
            pBehind = pBehind.next
        return pBehind

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node5 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
S = Solution()
print(S.FindKthToTail(node1, 2).val)
