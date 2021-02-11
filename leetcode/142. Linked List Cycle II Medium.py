# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return
        slow = fast = head
        flag = 0
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = 1
                break
        if not flag:
            return
        l = 0
        while slow.next != fast:
            slow = slow.next
            l += 1
        slow, fast = head, head
        while l >= 0:
            fast = fast.next
            l -= 1
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
