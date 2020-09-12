# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_helper(root, sum, currentpath):
    if root is None:
        return sum
    currentpath += str(root.val)
    if root.left is None and root.right is None:
        sum += int(currentpath)
        return sum
    else:
        sum = recursive_helper(root.right, sum, currentpath)
        sum = recursive_helper(root.left, sum, currentpath)
    return sum


def find_sum_of_path_numbers(root):
    sum = recursive_helper(root, 0, '')
    return sum


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
