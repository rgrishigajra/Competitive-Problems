class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        return


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(row, col, word, res, node):
            if len(res) == len(words):
                return
            if 0 > row or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            char = board[row][col]
            if char not in node.children:
                return
            new = node.children[char]
            if new.is_end:
                res.append(word+char)
                new.is_end = False
            board[row][col] = '#'
            dfs(row+1, col, word+char, res, new)
            dfs(row, col+1, word+char, res, new)
            dfs(row-1, col, word+char, res, new)
            dfs(row, col-1, word+char, res, new)
            board[row][col] = char
            if not new.children:
                del node.children[char]
        trie = Trie()
        res = []
        node = trie.root
        for word in words:
            trie.insert(word)
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, '', res, node)
        return res
