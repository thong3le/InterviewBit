class MinStack:
    stack = []
    min = []
    
    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self, x):
        self.stack.append(x)
        if not self.min or self.min[-1] >= x:
            self.min.append(x)
    
    def pop(self):
        if self.stack:
            x = self.stack.pop()
            if x == self.min[-1]:
                self.min.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else -1
    
    def getMin(self):
        return self.min[-1] if self.min else -1