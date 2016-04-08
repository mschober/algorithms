pali = "abba"
not_pali = "abbcdca"

# Walk the list with two pointers
# Second pointer gets to middle when first finishes
# push slow pointer elements into stack
# Once middle, pop stack and compare

class Stack:
    
    def __init__(self):
        self.elements = []
        
    def push(self, element):
        self.elements = list(element) + self.elements
        
    def pop(self):
        top = self.elements[0]
        self.elements = self.elements[1:]
        return top
    
s = Stack()
s.push('a')
s.push('a')
s.push('b')
print s.elements

print s.pop()
print s.pop()
print s.pop()

print len(s.elements)
