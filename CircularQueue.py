class CircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        "print k"
        self.len = k
        self.currlen = 0
        self.queue = [None] * k
        self.head = -1
        self.tail = -1


    def enQueue(self, value: int):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        tail = (self.tail+1) % self.len
        self.queue[tail] = value
        self.tail = tail
        self.currlen += 1
        if self.currlen == 1:
            self.head = 0

        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """

        if self.isEmpty():
            return False

        self.head = (self.head+1) % self.len
        self.currlen -= 1
        if self.isEmpty():
            self.head = -1
            self.tail = -1

        return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1

        return self.queue[self.head]


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1

        return self.queue[self.tail]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.currlen == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.currlen == self.len



obj = CircularQueue(5)
param_1 = obj.enQueue(4)
print(param_1)
param_11 = obj.enQueue(5)
param_12 = obj.enQueue(6)
param_13 = obj.enQueue(3)
print(param_13)
param_2 = obj.deQueue()
print(param_2)
param_3 = obj.Front()
print(param_3)
param_4 = obj.Rear()
print(param_4)
param_5 = obj.isEmpty()
print(param_5)
param_6 = obj.isFull()
print(param_6)