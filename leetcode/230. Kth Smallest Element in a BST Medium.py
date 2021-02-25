# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        stack = []
        idx = 0
        ans = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            idx += 1
            if idx == k:
                return node.val
            node = node.right

        return None
