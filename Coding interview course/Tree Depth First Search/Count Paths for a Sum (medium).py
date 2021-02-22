class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count_paths(self, root, S):
        return self.count_paths_recursive(root, S, [])

    def count_paths_recursive(self, currentNode, S, currentPath):
        if currentNode is None:
            return 0

        # add the current node to the path
        currentPath.append(currentNode.val)
        pathCount, pathSum = 0, 0
        # find the sums of all sub-paths in the current path list
        for i in range(len(currentPath)-1, -1, -1):
            pathSum += currentPath[i]
            # if the sum of any sub-path is equal to 'S' we increment our path count.
            if pathSum == S:
                pathCount += 1

        # traverse the left sub-tree
        pathCount += self.count_paths_recursive(
            currentNode.left, S, currentPath)
        # traverse the right sub-tree
        pathCount += self.count_paths_recursive(
            currentNode.right, S, currentPath)

        # remove the current node from the path to backtrack
        # we need to remove the current node while we are going up the recursive call stack
        del currentPath[-1]

        return pathCount


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
