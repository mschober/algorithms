import unittest
from tree import Tree

class TestTree(unittest.TestCase):

    def test_single_node(self):
        tree = Tree(1)
        self.assertEquals(1, tree.nodes())
