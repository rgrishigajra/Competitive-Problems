# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        newHead = None
        t1, t2 = None, head
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        cur = head
        while n >= k:
            prev = None
            for _ in range(k):
                nex = cur.next
                cur.next = prev
                prev = cur
                cur = nex
            if not newHead:
                newHead = prev
            if t1:
                t1.next = prev
            t2.next = cur
            t1 = t2
            t2 = t2.next
            n -= k
        return newHead
