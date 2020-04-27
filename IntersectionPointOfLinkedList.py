class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class IntersectionPointOfLinkedList(object):

    def getIntersectionNode(self, headA: Node, headB: Node):
        listA, listB = headA,headB
        lenA, lenB = 0,0

        while listA is not None:
            lenA += 1
            listA = listA.nextNode

        while listB is not None:
            lenB += 1
            listB = listB.nextNode

        listA, listB = headA,headB

        if lenA > lenB:
            for i in range(lenA - lenB):
                listA = listA.nextNode

        elif lenB > lenA:
            for i in range(lenB-lenA):
                listB = listB.nextNode

        while listA != listB:
            listA = listA.nextNode
            listB = listB.nextNode
        return listA








