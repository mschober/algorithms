import unittest
from linked_list import *

class TesstLinkedList(unittest.TestCase):

    def test_single_element_list(self):
        list = LinkedList(1)
        self.assertEqual(1, len(list))

    def test_two_nodes(self):
        list = LinkedList(1)
        list.addFirst(2)
        self.assertEqual(2, len(list))

    def test_get_next(self):
        list = LinkedList(1)
        list.addFirst(2)
