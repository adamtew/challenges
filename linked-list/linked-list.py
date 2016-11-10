class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def next(self):
        return self.next


class LinkedList:
    def __init__(self, node=None):
        if node is None:
            self.head = None
        else:
            self.head = node

    def print_list(self):
        if self.head is not None:
            self._print_list(self.head)

    def _print_list(self, node):
        if node is not None:
            print node.data
            self._print_list(node.next)

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self._insert(self.head, data)

    def _insert(self, node, data):
        if node.next is None:
            node.next = Node(data)
        else:
            self._insert(node.next, data)

linked_list = LinkedList()

for x in range(1, 21):
    linked_list.insert(x)

linked_list.print_list()
