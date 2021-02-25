# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        ans = deque([])
        q = [root]
        while q:
            node = q.pop()
            ans.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
