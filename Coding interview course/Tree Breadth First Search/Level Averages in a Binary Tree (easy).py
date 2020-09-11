# Given a binary tree, populate an array to represent the averages of all of its levels.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    q = [root]
    while q:
        lvl_avg = 0
        l = len(q)
        for _ in range(l):
            node = q.pop(0)
            lvl_avg += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(lvl_avg/l)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
