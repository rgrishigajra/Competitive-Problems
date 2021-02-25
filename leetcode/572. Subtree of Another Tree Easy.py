class Solution:
    def preorder(self, node):
        if node == None:
            return "null"

        return "#" + str(node.val) + self.preorder(node.left) + self.preorder(node.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        trees = self.preorder(s)
        treet = self.preorder(t)

        return treet in trees


class Solution:
    def equals(self, s, t):
        if s is None or t is None:
            return s == t
        if s.val != t.val:
            return False
        return self.equals(s.left, t.left) and self.equals(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None or t is None:
            return s == t
        check = False
        if s.val == t.val:
            check = (self.equals(s.left, t.left)
                     and self.equals(s.right, t.right))
        return check or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


class Solution:
    def isSubtree(self, s, t):
        from hashlib import sha256

        def hash_(x):
            S = sha256()
            S.update(x.encode())
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle

        merkle(s)
        merkle(t)

        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or
                    dfs(node.left) or dfs(node.right))

        return dfs(s)
