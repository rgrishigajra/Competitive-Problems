class Solution:
    def flatten(self, root: TreeNode) -> None:
        # Handle the null scenario
        if not root:
            return root
        while root:
            if root.left:
                rightmost = root.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
