# Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    lvl = 0
    q = [root]
    while q:
        lvl += 1
        no_of_nodes = len(q)
        for _ in range(no_of_nodes):
            node = q.pop(0)
            if not node.left and not node.right:
                return lvl
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


def find_minimum_depth_recursive(root):
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return find_minimum_depth(root.right)+1
    if root.right is None:
        return find_minimum_depth(root.left)+1
    return (1 + min(find_minimum_depth(root.left), find_minimum_depth(root.right)))


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)) +
          "recursive: " + str(find_minimum_depth_recursive(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)) +
          "recursive: " + str(find_minimum_depth_recursive(root)))


main()
