# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2, result_head = l1, l2, None
        n1, n2 = 0, 0
        while node1:
            node1 = node1.next
            n1 += 1

        while node2:
            node2 = node2.next
            n2 += 1
        node1, node2 = l1, l2
        result = result_head
        while n1 > 0 and n2 > 0:
            total = 0
            if n1 >= n2:
                total += node1.val
                n1 -= 1
                node1 = node1.next
            if n2 > n1:
                total += node2.val
                n2 -= 1
                node2 = node2.next
            result = ListNode(total, result)
        temp_list = result
        final = result_head
        carry = 0
        while result:
            total = result.val + carry
            carry = total // 10
            total = total % 10
            final = ListNode(total, final)
            result = result.next
        if carry:
            final = ListNode(carry, final)
        return final
