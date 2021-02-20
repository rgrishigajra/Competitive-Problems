# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, p: int, q: int) -> ListNode:
        if p == q or not head:
            return head
        prev, node, idx = None, head, 1
        while node and idx < p:
            prev = node
            node = node.next
            idx += 1
        prev_head = prev
        curr_head = node
        nex = None
        while node and idx < q+1:
            idx += 1
            nex = node.next
            node.next = prev
            prev = node
            node = nex
        curr_head.next = nex
        if prev_head:
            prev_head.next = prev
        else:
            head = prev
        return head
