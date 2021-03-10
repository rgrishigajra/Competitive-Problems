class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.h = height
        self.w = width
        self.food_idx = 0
        self.food = food
        self.grid = collections.defaultdict(int)
        self.cord = [0, 0]
        self.time = 1
        self.length = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        if direction == 'U':
            self.cord[0] -= 1
        elif direction == 'D':
            self.cord[0] += 1
        elif direction == 'L':
            self.cord[1] -= 1
        elif direction == 'R':
            self.cord[1] += 1
        if self.cord[0] < 0 or self.cord[0] >= self.h:
            return -1
        if self.cord[1] < 0 or self.cord[1] >= self.w:
            return -1
        r, c = self.cord
        if self.food_idx < len(self.food) and r == self.food[self.food_idx][0] and c == self.food[self.food_idx][1]:
            self.length += 1
            self.food_idx += 1
        elif self.grid[(r, c)] > self.time-self.length:
            return -1
        self.time += 1
        self.grid[(r, c)] = self.time
        return self.length


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
