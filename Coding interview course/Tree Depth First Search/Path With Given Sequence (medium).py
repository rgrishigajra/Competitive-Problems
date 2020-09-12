# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_helper(root, sequence, current_path):
    if root is None:
        return False
    current_path.append(root.val)
    # below line cuts out extra computation as soon as a different node arrives thats not in path
    if len(sequence) < len(current_path) or root.val != sequence[len(current_path)-1]:
        return False
    if current_path == sequence and root.left is None and root.right is None:
        return True
    else:
        return recursive_helper(root.left, sequence, current_path.copy()) or recursive_helper(root.right, sequence, current_path.copy())
    return False


def find_path(root, sequence):
    return recursive_helper(root, sequence, [])


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
