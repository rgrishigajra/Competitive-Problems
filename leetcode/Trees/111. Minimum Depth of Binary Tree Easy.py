# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth_iterative_BFS(self, root: TreeNode) -> int:
        current_lvl = 0
        if not root:
            return 0
        q = [root]
        while q:
            current_lvl += 1
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if not node.right and not node.left:
                    return current_lvl
        return current_lvl


class Solution:
    def minDepth_recursive(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        if not root.right:
            return self.minDepth(root.left) + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
