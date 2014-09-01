import unittest
from linked_list import *

class TestLinkedList(unittest.TestCase):
    '''This is the absolute vanilla linked list implementation
       I can print the list
       I can add a node to the front of the list
       I can create a list
    '''

    def test_empty_list(self):
        ll = LinkedList()
        self.assertEqual(str(ll), "")

    def test_single_node(self):
        ll = LinkedList(1)
        self.assertEquals(str(ll), "1")

    def test_add_before(self):
        ll = LinkedList()
        ll.add_before(4)
        ll.add_before(3)
        ll.add_before(2)
        ll.add_before(1)
        self.assertEquals(str(ll), "1 2 3 4")

    def test_add_after(self):
        ll = LinkedList()
        ll.add_after(1)
        ll.add_after(2)
        ll.add_after(3)
        ll.add_after(4)
        self.assertEquals(str(ll), "1 2 3 4")

    def test_reverse(self):
        ll = LinkedList()
        ll.add_before(1)
        ll.add_before(2)
        ll.add_before(3)
        ll.add_before(4)
        ll.reverse()
        self.assertEllqual(str(ll), "1 2 3 4")


