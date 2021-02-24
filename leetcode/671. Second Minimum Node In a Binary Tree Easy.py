# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        q = [root]
        mini, min2 = math.inf, math.inf
        while q:
            node = q.pop()
            if node.val < mini:
                min2 = mini
                mini = node.val
            elif mini != node.val and node.val < min2:
                min2 = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return min2 if min2 != math.inf else -1
