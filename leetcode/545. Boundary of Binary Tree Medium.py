# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def _leftboundary(self, node):
        if not node or not (node.left or node.right):
            return
        self.boundary.append(node.val)
        if not node.left:
            self._leftboundary(node.right)
        else:
            self._leftboundary(node.left)

    def _rightboundary(self, node):
        if not node or not (node.left or node.right):
            return
        if not node.right:
            self._rightboundary(node.left)
        else:
            self._rightboundary(node.right)
        self.boundary.append(node.val)

    def _leaves(self, node):
        if not node:
            return
        if not (node.left or node.right):
            self.boundary.append(node.val)

        self._leaves(node.left)
        self._leaves(node.right)

    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.boundary = [root.val]
        self._leftboundary(root.left)
        self._leaves(root.left)
        self._leaves(root.right)
        self._rightboundary(root.right)
        return self.boundary
