class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None



class createLinkedList(object):

    def __init__(self):
        self.head = None

    def addAtStart(self, data):
        newnode = node(data)
        if not self.head:

            self.head = newnode

        else:

            newnode.next = self.head
            self.head = newnode

    def reverse(self):

        prev = None
        current = self.head

        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


    def print(self):

        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next










linkedlist = createLinkedList()
linkedlist.addAtStart(12)
linkedlist.addAtStart(22)
linkedlist.print()
linkedlist.reverse()
linkedlist.print()



