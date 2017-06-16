class Stack():
    def __init__(self):
        self.Stack=[]

    def empty(self):
        return self.Stack == []

    def push(self, data):
        self.Stack.append(data)


    def pop(self):
        data = self.Stack[-1]
        del self.Stack[-1]
        return data

    def peek(self):
        return self.Stack[-1]

    def size(self):
        return len(self.Stack)




stack = Stack()
stack.push(3)
stack.push(4)
stack.push(9)
stack.push(16)
print(stack.peek())
print(stack.size())
stack.pop()
stack.pop()
print(stack.size())
print(stack.peek())
