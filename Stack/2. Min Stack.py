class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []
        
    def push(self, val: int) -> None:
        self.stack += [val]
        if self.min_val:
            self.min_val += [min(val, self.min_val[-1])]
        else:
            self.min_val += [val]

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_val = self.min_val[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
