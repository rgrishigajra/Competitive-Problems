class MinStack:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        min_element = self.getMin()
        min_element = min(min_element, x)
        self.st.append((x, min_element))

    def pop(self) -> None:
        return self.st.pop(-1)

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        if self.st:
            return self.st[-1][1]
        else:
            return math.inf


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
