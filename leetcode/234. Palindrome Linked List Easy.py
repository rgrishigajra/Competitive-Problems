# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        slow , fast = head, head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        prev = None
        while slow is not None:
            nex = slow.next
            slow.nex = prev
            prev = slow
            slow = slow.next
        node = head
        while slow != None and node != None:
            if slow.val != node.val:
                return False
            slow = slow.next
            node = node.next 
        return True

