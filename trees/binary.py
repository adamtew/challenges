class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def next(self, next=None):
        if next is None:
            return self.next
        else:
            self.next = next

    def __str__(self):
        return "words"


class Tree:
    def __init__(self, node=None):
        if node is None:
            self.head = None
        else:
            self.head = node

    def __str__(self):
        return "head"

    def head(self, node=None):
        if node is None:
            return self.head
        else:
            self.head = node

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self.private_insert(self.head, data)

    """ highest at the top """
    def private_insert(self, node, data):
        if node.data > data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.private_insert(node.left, data)
        elif node.data < data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.private_insert(node.right, data)

    def print_tree(self):
        if self.head is not None:
            self.private_print(self.head)

    def private_print(self, node):
        if node is not None:
            if node.left is not None:
                self.private_print(node.left)
            print node.data
            if node.right is not None:
                self.private_print(node.right)

    def find(self, data):
        if self.head is not None:
            return self.private_find(self.head, data)
        else:
            return False

    def private_find(self, node, data):
        print 'finding ', data, ' currently at ', node.data
        if node.data == data:
            return node
        elif node.data > data and node.left is not None:
            return self.private_find(node.left, data)
        elif node.data < data and node.right is not None:
            return self.private_find(node.right, data)
        else:
            return None

    def delete(self):
        self.head = None


""" Driver Code """
node = Node(5)

print 'A node: ', node

tree = Tree(node)

for i in range(1, 20):
    tree.insert(i)

# print tree
tree.print_tree()

print tree.find(20)
