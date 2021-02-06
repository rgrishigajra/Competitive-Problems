class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        carry = 0
        answer_head = ListNode(None)
        answer = answer_head
        while node1 is not None or node2 is not None:
            val1 = node1.val if node1 is not None else 0
            val2 = node2.val if node2 is not None else 0
            total = val1 + val2 + carry
            carry = total // 10
            answer.next = ListNode(total % 10)
            answer = answer.next
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
        if carry:
            answer.next = ListNode(carry)
        return answer_head.next
