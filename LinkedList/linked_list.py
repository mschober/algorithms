class LinkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        self.list_length = 1 if value else 0

    def length(self):
        return self.list_length

    def __repr__(self):
        repr_str = ""
        repr_str += str(self.value) if self.value

    def add_after(self, value):
        self.next = LinkedList(value)
        self.list_length += 1
