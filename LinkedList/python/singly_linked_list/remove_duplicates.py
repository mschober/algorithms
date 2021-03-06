class LL:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def append(self, node):
        node.next = self
        #self.next = node
        return node
        
    def __repr__(self):
        #print 'before loop'
        curr = self
        rtr = str(curr.data)
        while curr.next != None:
            curr = curr.next
            rtr += str(curr.data)
           #print 'in loop'
        return rtr
    
    def __str__(self):
        return self.__repr__()
        
lls = [
    [3, LL(1).append(LL(3)).append(LL(4)), LL(1).append(LL(4))],
    [3, LL(1).append(LL(3)).append(LL(3)).append(LL(4)), LL(1).append(LL(4))],
    [3, None, None],
    [3, LL(1), LL(1)],
    [3, LL(3), None],
    [3, LL(3).append(LL(3)).append(LL(3)).append(LL(4)), LL(4)],
    [4, LL(4).append(LL(4)), None],
    [6, LL(6).append(LL(1)), LL(1)],
    [6, LL(1).append(LL(6)), LL(1)],
    [5, LL(1).append(LL(5)).append(LL(5)), LL(1)]
]

def remove_match(ll, rm):
    if not ll:
        return None
    
    curr = ll
    while curr.data == rm and curr.next:
        curr = curr.next
        ll = curr
    while curr.next != None:
        if curr.next.data == rm:
            #print 'remove %s' % curr.next.data
            curr.next = curr.next.next
        else:
            curr = curr.next
            
    if not curr.next and curr.data == rm:
        return None
    
    return ll

for test in lls:
    print "running %s" % str(test[1])
    run_result = remove_match(test[1], test[0])
    fail_string = "Testing %s should be %s, but was %s" % (str(test[1]), str(test[2]), str(run_result))
    assert str(test[2]) == str(run_result), fail_string


    
    
    
    
    
    
    
    
    
    
    
