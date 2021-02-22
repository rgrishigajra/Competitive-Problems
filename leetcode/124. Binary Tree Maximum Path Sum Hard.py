# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rec(self, node):
        if not node:
            return 0
        l = max(self.rec(node.left), 0)
        r = max(self.rec(node.right), 0)
        self.max_sum = max(self.max_sum, l+r+node.val, node.val)
        return max(l, r)+node.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -math.inf
        self.rec(root)
        return self.max_sum
