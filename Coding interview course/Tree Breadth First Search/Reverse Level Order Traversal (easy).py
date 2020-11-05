
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if not root:
        return root
    stack = [root]
    while stack:
        level = []
        for _ in range(len(stack)):
            node = stack.pop(0)
            if node != None:
                stack.append(node.left)
                stack.append(node.right)
                level.append(node.val)
        if level:
            result.insert(0, level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
