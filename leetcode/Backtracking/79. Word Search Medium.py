class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        for row in range(self.rows):
            for col in range(self.cols):
                if self.check(row,col,word):
                    return True
        return False
    def check(self,row,col,pattern):
        if not pattern:
            return True
        if row > -1 and row <self.rows and col >-1 and col < self.cols and self.board[row][col] == pattern[0]:
            self.board[row][col] = '#'
            if self.check(row-1,col,pattern[1:]) or self.check(row +1,col,pattern[1:]) or  self.check(row,col-1,pattern[1:]) or self.check(row,col+1,pattern[1:]):
                return True
            else:
                self.board[row][col] = pattern[0]
                return False
        return False