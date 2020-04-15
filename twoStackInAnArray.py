class twoStackInAnArray:

    def __init__(self, n):

        self.arraysize = n
        self.arr = [None] * n
        self.stack1 = -1
        self.stack2 = self.arraysize


    def pushStack1(self, data):

        if (self.stack1 < self.stack2 - 1) :
            self.stack1 = self.stack1 + 1
            self.arr[self.stack1] = data
        else:

            print("Stack Overflow")


    def pushStack2(self, data):
        if (self.stack1 < self.stack2 - 1):
            self.stack2 = self.stack2 - 1
            self.arr[self.stack2] = data
        else:

            print("Stack Overflow")


    def popStack1(self):

        if self.stack1 >= 0:
            x = self.arr[self.stack1]
            self.stack1 =  self.stack1 - 1
            return x
        else:

            print("Stack Underflow")

    def popStack2(self):

        if self.stack2 < self.arraysize:
            x = self.arr[self.stack2]
            self.stack2 =  self.stack2 + 1
            return x
        else:
            print("Stack Underflow")



t = twoStackInAnArray(5)
t.pushStack1(5)
t.pushStack2(10)
t.pushStack2(15)
t.pushStack1(11)
t.pushStack2(7)

print("Popped element from stack1 is " + str(t.popStack1()))
t.pushStack2(40)
print("Popped element from stack2 is " + str(t.popStack2()))




