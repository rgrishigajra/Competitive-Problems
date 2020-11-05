class Solution:
    def isValidBSTRecursive(self, root: TreeNode) -> bool:
        def helper(root, lower, upper):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return helper(root.right, root.val, upper) and helper(root.left, lower, root.val)
        return helper(root, -math.inf, math.inf)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        s = [(root, -math.inf, math.inf)]
        while s:
            [node, lower, upper] = s.pop()
            if node.val >= upper or node.val <= lower:
                return False
            if node.left:
                s.append((node.left, lower, node.val))
            if node.right:
                s.append((node.right, node.val, upper))
        return True
