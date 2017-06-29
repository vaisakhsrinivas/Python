class QusingStack():
    def __init__(self):
        self.QusingStack=[]

    def empty(self):
        return self.QusingStack == []

    def push(self, data):
        self.QusingStack.append(data)


    def pop(self):
        return self.QusingStack.pop()

    def peek(self):
        return self.QusingStack[-1]

    def size(self):
        return len(self.QusingStack)


class Stack():
    def __init__(self):
        self.Stack1=QusingStack()
        self.Stack2=QusingStack()

    def nq(self,data):
        self.Stack1.push(data)

    def dq(self):
        if not self.Stack1.empty():
            while self.Stack1.size() >0:
                data = self.Stack1.pop()
                self.Stack2.push(data)
            value = self.Stack2.pop()
            return value



if __name__ == "__main__":
    q = Stack()
    q.nq(1)
    q.nq(2)
    q.nq(3)
    q.nq(5)
    q.nq(6)
    v = q.dq()
    print(v)
