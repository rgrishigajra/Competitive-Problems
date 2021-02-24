# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.pre_idx = 0
        self.inorder_map = {val: idx for idx, val in enumerate(inorder)}
        return self.helper(0, len(inorder), preorder)

    def helper(self, left_idx, right_idx, preorder):
        if left_idx >= right_idx:
            return None
        val = preorder[self.pre_idx]
        inorder_idx = self.inorder_map[val]
        self.pre_idx += 1
        node = TreeNode(val)
        node.left = self.helper(left_idx, inorder_idx, preorder)
        node.right = self.helper(inorder_idx+1, right_idx, preorder)
        return node
