import unittest
from linked_list import *

class TestLinkedList(unittest.TestCase):

    def test_empty_list(self):
        ll = LinkedList()
        self.assertEqual(ll.length(), 0)
        self.assertEqual(str(ll), "")
        self.assertNotEqual(ll, None)

    def test_single_node(self):
        ll = LinkedList(1)
        self.assertEquals(ll.length(), 1)

    def test_print_list(self):
        ll = LinkedList(1)
        self.assertEquals(str(ll), "1")

    def test_insert_node(self):
        ll = LinkedList(1)
        ll.add_after(2)
        self.assertEquals(ll.length(), 2)

    #def test_print_list(self):
    #    ll = LinkedList(1)
    #    ll.insert(2)
    #    self.assertEquals(str(ll), "1 2")

