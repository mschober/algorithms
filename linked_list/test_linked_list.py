import unittest
from linked_list import *

class TesstLinkedList(unittest.TestCase):

    def test_single_element_list(self):
        list = LinkedList(1)
        self.assertEqual(1, len(list))
