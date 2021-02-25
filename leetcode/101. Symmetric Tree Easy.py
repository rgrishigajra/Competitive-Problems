# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recurs(node1, node2):
            if not node1 or not node2:
                return node1 == node2
            if node1.val != node2.val:
                return False
            return recurs(node1.left, node2.right) and recurs(node1.right, node2.left)
        return recurs(root.left, root.right)
