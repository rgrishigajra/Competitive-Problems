# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        p_val = p.val
        q_val = q.val
        while root:
            if p_val < root.val and q_val < root.val:
                root = root.left
            elif p_val > root.val and q_val > root.val:
                root = root.right
            else:
                return root
        return None
