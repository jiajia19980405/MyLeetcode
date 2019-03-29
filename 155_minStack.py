class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.que = []

    def push(self, x):
        self.que.append(x)
        i = len(self.que) -1
        while i != 0 and self.que[i-1] < self.que[i] :
            self.que[i], self.que[i-1] = self.que[i-1], self.que[i]
            i -= 1
        
        self.stack.append([x,i])
        

    def pop(self):
        temp = self.stack[-1][1]
        del self.que[temp]
        self.stack.pop()


    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.que[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()