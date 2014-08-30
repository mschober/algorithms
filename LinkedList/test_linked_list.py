import unittest
from linked_list import *

class TestLinkedList(unittest.TestCase):

    def test_single_node(self):
        ll = LinkedList(1)
        self.assertEquals(ll.length(), 1)
