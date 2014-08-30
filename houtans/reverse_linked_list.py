class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def hasNext(self):
        return True if self.next else False

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, value=None):
        self.head = Node(value) if value else None

    def next(self):
        return self.head.next

    def insert(self, value):
        #print "inserting {0}".format(value)
        node = self.head
        if node:
            #print "head exists for inserting {0}".format(self.head.value)
            while node.hasNext():
                node = node.next
            self.head = self.head.next
        else:
            #print "adding headnode"
            self.head = Node(value)


    def reverse(self):
        return self

    def __repr__(self):

        def append_node_value(out, node):
            return out + str(node) + '\n'

        out = ""
        node = self.head
        while node.hasNext():
            out = append_node_value(out, node)
            node = node.next
        else:
            out = append_node_value(out, node)
        return out

#print 2 elements
ll = LinkedList()
ll.insert(1)
ll
ll.insert(2)
ll
ll.insert(3)
ll
ll.insert(4)
ll
ll.insert(5)
ll

#reverse list
rl = ll.reverse()
rl
