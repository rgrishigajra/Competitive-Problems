# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, node, pathCur, allPaths, targetSum):
        if not node:
            return
        pathCur.append(node.val)
        if targetSum == node.val and not node.left and not node.right:
            allPaths.append(pathCur.copy())
        else:
            self.helper(node.left, pathCur, allPaths, targetSum-node.val)
            self.helper(node.right, pathCur, allPaths, targetSum-node.val)
        pathCur.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        allPaths = []
        self.helper(root, [], allPaths, targetSum)
        return allPaths
