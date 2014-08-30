class Tree:

    def __init__(self, datum=None, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right

    def insert(self, datum):
        if datum < self.datum:
            if self.left:
                self.left.insert(datum)
            else:
                self.left = Tree(datum)

        else:
            if self.right:
                self.right.insert(datum)
            else:
                self.right = Tree(datum)

    def in_order_print(self, node=self.node):
        if self.left:
            self.in_order_print(self.left)
        print(self.datum)
        if self.right:
            self.in_order_print(self.right)
