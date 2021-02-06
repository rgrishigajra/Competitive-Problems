# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = -math.inf
        current_level = 0
        max_sum_level = 0
        if not root:
            return root
        q = [root]
        while q:
            n = len(q)
            current_level += 1
            current_level_sum = 0
            for _ in range(n):
                node = q.pop(0)
                current_level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_sum_level = current_level
        return max_sum_level
