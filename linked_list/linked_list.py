class Node:

    data = None
    next = None

    def __init__(self, data=None):
        self.data = data


class LinkedList:

    head = None
    length = 0

    def __init__(self, data):
        self.addNode(data)
        self.len = 0

    def addNode(self, data):
        new_node = Node(data)
        if self.head:
            self.head.next = new_node
            self.head = new_node
        else:
            self.head = new_node
        self.length = self.length + 1

    def __len__(self):
        return self.length
