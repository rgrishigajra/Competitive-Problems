# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(
            root.left, p, q) if root.left else None
        right = self.lowestCommonAncestor(
            root.right, p, q) if root.right else None
        if left and right:
            return root
        else:
            if left:
                return left
            return right
