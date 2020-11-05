# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return root
        array = [root]
        direction = False
        while array:
            n = len(array)
            level = []
            direction = not direction
            for i in range(n):
                node = array.pop(0)
                if node.left:
                    array.append(node.left)
                if node.right:
                    array.append(node.right)
                if direction:
                    level.insert(len(level), node.val)
                else:
                    level.insert(0, node.val)
            result.append(level)
        return result
