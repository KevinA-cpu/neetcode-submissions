class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or self.minStack[-1][0] > val:
            self.minStack.append((val,len(self.stack)-1))

    def pop(self) -> None:
        if len(self.stack)-1 == self.minStack[-1][1]:
            self.minStack.pop();
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][0]
        
