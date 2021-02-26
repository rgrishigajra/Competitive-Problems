# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        qu = deque([[root, 0, 0]])
        dic = defaultdict(list)
        mini, maxi = math.inf, -math.inf
        ans = []
        while qu:
            for _ in range(len(qu)):
                node, row, col = qu.popleft()
                dic[col].append((row, node.val))
                if mini > col:
                    mini = col
                if maxi < col:
                    maxi = col
                if node.left:
                    qu.append([node.left, row+1, col-1])
                if node.right:
                    qu.append([node.right, row+1, col+1])
        for col in range(mini, maxi+1):
            ans.append([a[1] for a in sorted(dic[col])])
        return ans
