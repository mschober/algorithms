class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) 

class LinkedList:

    def __init__(self, value=None):
        self.head = None

        if value:
            self.add_before(value)

    def add_before(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def add_after(self, value):
        if self.head:
            self.add_after_recur(self.head, Node(value))
        else:
            self.add_before(value)

    def add_after_recur(self, curr, node):
        if curr.next:
            return self.add_after_recur(curr.next, node)
        else:
            curr.next = node

    def reverse(self):
        reversed = LinkedList()
        curr = self.head
        while curr.next:
            reversed.add_before(curr.value)
        self.head = reversed.head

    def reverse_bad(self):
        if self.head:
            self.reverse_recur(self.head)

    def reverse_recur(self, curr):
        #4 3 2 1
        #1: 4.next = 3
        #1: 
        if curr.next:
            self.reverse_recur(curr.next).next = curr
            curr.next = None
            ##
            # Stack trace
            trace = LinkedList()
            trace.head = curr
            print "stack: " + str(trace)
        else:
            return curr


    def __repr__(self):
        if self.head:
            return self.construct_repr(self.head)
        else:
            return ""

    def construct_repr(self, node):
        def str_with_delim(val, delim=" "):
            return str(val) + delim

        if node.next:
            return str_with_delim(node) + self.construct_repr(node.next)
        else:
            return str(node)
