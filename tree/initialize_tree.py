from tree import CBOrdTree
from random import randrange

tree = CBOrdTree

def ten_node_tree():
    for val in range(20):
        tree.addNode(randrange(1, 101))

tree.printTree()
