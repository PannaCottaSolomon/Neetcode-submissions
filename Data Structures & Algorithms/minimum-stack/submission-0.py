class MinStack:

    def __init__(self):
        self.stack = []
        self.idx = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.idx += 1

    def pop(self) -> None:
        self.stack.pop()
        self.idx -= 1

    def top(self) -> int:
        num = self.stack[self.idx]
        # print(self.stack)
        # print(self.idx)
        # print(num)
        return num

    def getMin(self) -> int:
        return min(self.stack)
