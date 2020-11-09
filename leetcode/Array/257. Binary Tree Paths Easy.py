# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        stack = [(root, "")]
        res = []
        while stack:
            node, path = stack.pop()
            path += "->"+str(node.val)
            if node.left == None and node.right == None:
                res.append(path[2:])
            else:
                if node.left != None:
                    stack.append((node.left, path))
                if node.right != None:
                    stack.append((node.right, path))
        return res
