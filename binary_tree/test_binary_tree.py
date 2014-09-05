import unittest
from binary_tree import *

class TestBST(unittest.TestCase):

    def test_empty_tree(self):
        tree = BST()
        self.assertTrue(tree)

    def test_tree_root(self):
        tree = BST()
        tree.add(5)
        self.assertEqual(tree.inorder(), "5")

    def test_two_node_left(self):
        tree = BST()
        tree.add(5)
        tree.add(4)
        self.assertEqual(tree.inorder(), "4 5")

    def test_10_nodes(self):
        tree = BST()
        tree.add(5)
        tree.add(4)
        tree.add(100)
        tree.add(95)
        tree.add(2)
        tree.add(1)
        tree.add(2)
        tree.add(4)
        tree.add(3)
        tree.add(6)
        self.assertEqual(tree.inorder(), "1 2 3 4 5 6 95 100")
