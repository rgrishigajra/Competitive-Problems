# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.treeDiameter = 1

    def helper(self, node):
        if not node:
            return 0
        left_child = self.helper(node.left)
        right_child = self.helper(node.right)
        self.treeDiameter = max(
            self.treeDiameter, left_child + right_child+1)
        return max(left_child, right_child)+1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.treeDiameter-1
