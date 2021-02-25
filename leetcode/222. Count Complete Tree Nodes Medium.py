# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def get_heights(self, root):
        node = root
        l, r = 0, 0
        while node:
            node = node.left
            l += 1
        while root:
            root = root.right
            r += 1
        return [l, r]

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        l, r = self.get_heights(root)
        if l == r:
            return 2**l - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
