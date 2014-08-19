
class LinkedList:

    class Node:

        data = None
        next = None

        def __init__(self, data=None):
            self.data = data

    head = None
    length = 0

    def __init__(self, data):
        self.addFirst(data)

    def addFirst(self, data):
        new_node = LinkedList.Node(data)
        if self.head:
            node_tmp = self.head
            self.head = new_node
            new_node.next = node_tmp
        else:
            self.head = new_node
        self.length = self.length + 1

    def __len__(self):
        return self.length
