# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = collections.deque([root])
        ans = []
        while result:
            level = []
            for _ in range(len(result)):
                node = result.popleft()
                level.append(node.val)
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
            ans.append(level)
        return ans
