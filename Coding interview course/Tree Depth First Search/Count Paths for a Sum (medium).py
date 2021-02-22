class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def r(node, path, s):
    if not node:
        return 0
    cur_path = [*path, node.val]
    cur_sum = 0
    start = 0
    sumi = 0
    for end, val in enumerate(cur_path):
        cur_sum += val
        while cur_sum > s:
            cur_sum -= cur_path[start]
            start += 1
        if cur_sum == s:
            sumi += 1
    return r(node.left, cur_path, s) + r(node.right, cur_path, s) + sumi


def count_paths(root, S):
    return r(root, [], S)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
