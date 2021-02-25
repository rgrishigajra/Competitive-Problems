# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        stack = []
        ans = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans
