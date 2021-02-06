# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(None)
        res = dummy
        heap = []
        if not lists:
            return dummy.next
        for ind, li in enumerate(lists):
            if li:
                heapq.heappush(heap, (li.val, ind, li))
        while heap:
            val, ind, node = heapq.heappop(heap)
            res.next = ListNode(val)
            res = res.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, ind, node))
        return dummy.next
