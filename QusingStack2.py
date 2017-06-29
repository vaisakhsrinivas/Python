class QusingStack2(object):
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def enqueue(self,element):
        self.instack.append(element)
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
q=QusingStack2()
for i in range(10):
    q.enqueue(i)
for i in range(10):
    print (q.dequeue())