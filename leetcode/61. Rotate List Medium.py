# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        node = head
        l = 0
        while node.next is not None:
            node = node.next
            l += 1
        k = l - k % (l+1)
        node.next = head
        while k >= 0:
            k -= 1
            node = node.next
        ans = node.next
        node.next = None
        return ans
