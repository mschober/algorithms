class BST:

    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.root = None

    def add(self, data):
        def recur_add(node, data):
            if not node:
                return self.Node(data)
            elif node.data == data:
                return node
            elif data < node.data:
                node.left = recur_add(node.left, data)
            else:
                node.right = recur_add(node.right, data)
            return node
        if self.root:
            self.root = recur_add(self.root, data)
        else:
            self.root = recur_add(None, data)

    def inorder_temp(self):
        out_str = ""
        out_str += str(self.root.left) + ' '
        out_str += str(self.root)
        return out_str

    def inorder(self):
        out_str = ""
        def recur_inorder(node, out_str):
            if node:
                out_str = recur_inorder(node.left, out_str)
                out_str += str(node) + ' '
                out_str = recur_inorder(node.right, out_str)
            return out_str
        return recur_inorder(self.root, out_str).strip()

    def __repr__(self):
        return self.inorder()
