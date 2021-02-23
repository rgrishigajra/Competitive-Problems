# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,node,maxi):
        if not node:
            return node
        if node.val>=maxi:
            self.count+=1
            maxi = node.val
        self.rec(node.left,maxi)
        self.rec(node.right,maxi)
        
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.rec(root,root.val)
        return self.count