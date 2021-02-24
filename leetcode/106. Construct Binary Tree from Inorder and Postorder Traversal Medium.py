# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.post_idx = len(postorder)-1
        self.hash_val = {val: idx for idx, val in enumerate(inorder)}
        return self.helper(0, len(postorder), postorder)

    def helper(self, left, right, postorder):
        if left >= right:
            return None
        val = postorder[self.post_idx]
        self.post_idx -= 1
        in_idx = self.hash_val[val]
        node = TreeNode(val)
        node.right = self.helper(in_idx+1, right, postorder)
        node.left = self.helper(left, in_idx, postorder)
        return node
