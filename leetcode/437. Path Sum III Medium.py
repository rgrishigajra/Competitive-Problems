# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root, S):
        self.s = S
        self.hash = collections.defaultdict(int)
        self.count = 0
        self.count_paths_recursive(root, 0)
        return self.count

    def count_paths_recursive(self, node, cur_sum):
        if node is None:
            return
        cur_sum += node.val
        if cur_sum == self.s:
            self.count += 1
        self.count += self.hash[cur_sum-self.s]
        self.hash[cur_sum] += 1
        self.count_paths_recursive(node.left, cur_sum)
        self.count_paths_recursive(node.right, cur_sum)
        self.hash[cur_sum] -= 1
