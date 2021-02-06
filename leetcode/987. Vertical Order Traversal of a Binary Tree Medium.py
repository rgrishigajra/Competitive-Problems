# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        q = [[root, 0]]
        min_col = math.inf
        max_col = -math.inf
        columns = collections.defaultdict(list)
        while q:
            row = []
            for _ in range(len(q)):
                (node, col) = q.pop(0)
                min_col = min(min_col, col - 1)
                max_col = max(max_col, col + 1)
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
                row.append([node.val, col])
            row.sort()
            for val, col in row:
                columns[col].append(val)
        result = []
        for i in range(min_col, max_col+1):
            if columns[i]:
                result.append(columns[i])
        return result
