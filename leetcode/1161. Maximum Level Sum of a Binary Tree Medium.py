# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        maxi = -math.inf
        lvl = 0
        max_lvl = 0
        while q:
            lvl += 1
            curr = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if curr > maxi:
                max_lvl = lvl
                maxi = curr
        return max_lvl
