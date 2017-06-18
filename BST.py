class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertnode(data,self.root)

    def insertnode(self, data, node):
        if data < node.data:
            if node.lchild:
                self.insertnode(data, node.lchild)
            else:
                node.lchild = Node(data)

        else:

            if node.rchild:
                self.insertnode(data, node.rchild)
            else:
                node.rchild = Node(data)


    def removenode(self, data, node):

        if not node:
            return node

        if data < node.data:
            node.lchild = self.removenode(data, node.lchild)
        elif data > node.data:
            node.rchild = self.removenode(data, node.rchild)

        else:

            if not node.lchild and not node.rchild:
                print("remove leaf node")
                del node
                return None

            if not node.lchild:

                print("remove single right child node")
                temp = node.rchild
                del node
                return  temp

            elif not node.rchild:

                print("remove single left child node")
                temp = node.lchild
                del node
                return temp

            tnode = self.predecessor(node.lchild)
            node.data = tnode.data
            node.lchild = self.removenode(tnode.data, node.lchild)

        return node

    def predecessor(self, node):

        if node.rchild:
            return self.predecessor(node.rchild)

        return node


    def remove(self, data):
        if self.root:
            self.root = self.removenode(data, self.root)


    def minval(self):
        if self.root:
            return self.min(self.root)

    def min(self, node):
        if node.lchild:
            return self.min(node.lchild)

        return node.data


    def maxval(self):
        if self.root:
            return self.max(self.root)

    def max(self, node):
        if node.rchild:
            return self.max(node.rchild)

        return node.data


    def traverse(self):
        if self.root:
            self.inorder(self.root)


    def inorder(self, node):

        if node.lchild:
            self.inorder(node.lchild)

        print ("%s" % node.data)

        if node.rchild:
            self.inorder(node.rchild)



bst = BST()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)
bst.remove(10)

print(bst.traverse())
