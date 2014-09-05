import unittest
from binary_tree import *

class TestBST(unittest.TestCase):

    #def test_empty_tree(self):
    #    tree = BST()
    #    self.assertTrue(tree)

    #def test_tree_root(self):
    #    tree = BST()
    #    tree.add(5)
    #    self.assertEqual(tree.inorder(), "5")

    def test_two_node_left(self):
        tree = BST()
        tree.add(5)
        tree.add(4)
        self.assertEqual(tree.inorder(), "4 5")
