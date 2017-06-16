class Queue():
    def __init__(self):
        self.Queue=[]

    def empty(self):
        return self.Queue == []

    def enqueue(self, data):
        self.Queue.append(data)


    def dequeue(self):
        data = self.Queue[0]
        del self.Queue[0]
        return data

    def peek(self):
        return self.Queue[0]

    def size(self):
        return len(self.Queue)




queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(9)
queue.enqueue(16)
print(queue.peek())
print(queue.size())
queue.dequeue()
queue.dequeue()
print(queue.size())
print(queue.peek())
