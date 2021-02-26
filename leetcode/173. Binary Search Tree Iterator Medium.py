# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.node = root

    def next(self) -> int:
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        self.node = self.stack.pop()
        ans = self.node
        self.node = self.node.right
        return ans.val

    def hasNext(self) -> bool:
        return self.stack or self.node


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
