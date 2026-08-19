class MinStack:

    def __init__(self):
        self.idx = -1
        self.minIdx = -1
        self.minimum = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.minimum) == 0:
            self.minimum.append(val)
        else:
            smaller = min(self.minimum[self.minIdx], val)
            self.minimum.append(smaller)
        self.stack.append(val)
        self.idx += 1
        self.minIdx += 1

    def pop(self) -> None:
        self.stack.pop()
        self.idx -= 1
        self.minimum.pop()
        self.minIdx -= 1

    def top(self) -> int:
        return self.stack[self.idx]

    def getMin(self) -> int:
        return self.minimum[self.minIdx]
