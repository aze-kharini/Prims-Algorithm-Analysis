#rename this file to PQBinaryHeap.py

class APQBinaryHeap:
    """ Maintain an collection of items, popping by lowest key.

        This implementation maintains the collection using a binary heap.
        Uses an internally-defined class Element to store the items as a
        key (i.e. priority) and value (i.e. the actual item) pair.
        Use this class by typing PQBinaryHeap.Element() etc.
    """
    class Element:
        """ An element with a key and value. """
        
        def __init__(self, k, v, i=None):
            self._key = k
            self._value = v
            self._index = i

        def __str__(self):
            return "["+str(self._key)+","+str(self._value)+"]"
        
        def __repr__(self):
            return self.__str__()

        def __eq__(self, other):
            """ Return True if this key equals the other key. """
            return self._key == other._key

        def __lt__(self, other):
            """ Return True if this key is less than the other key. """
            return self._key < other._key

        def _wipe(self):
            """ Set the instance variables to None. """
            self._key = None
            self._value = None
            self._index = None
        
        def setValue(self, new_value):
            self._value = new_value
        
        def getValue(self):
            return self._value
        
        value = property(getValue, setValue)


    def __init__(self):
        """ Create a PQ with no elements. """

        # this is an array-based heap, so you need to create
        # an empty python list, and then maintain it
        # properly in the add and remove-min methods.
        self._heap = []
        
    def __str__(self):
        """ Return a breadth-first string of the values. """
        string = ""
        for element in self._heap:
            string += str(element._key) + ":" + str(element._value) + "["+str(element._index)+"]" + ", "
        return string
    
    def __repr__(self):
        return self.__str__()
            
    # First, the four standard methods for the ADT

    def add(self, key, value):
        """ Add Element(key,value) to the heap. """
        new_element = self.Element(key,value, self.length()) # for appending it
        self._heap.append(new_element)
        self._upheap(self.length()-1)
        return new_element

    def min(self):
        """ Return the min priority key,value. """
        if self.length() > 0:
            return self._heap[0]
        return None

    def remove_min(self):
        """ Remove and return the min priority key,value. """
        min_element = self.min()
        self._heap[0] = self._heap[self.length()-1]
        self._heap[0]._index = 0
        self._heap.pop()
        self._downheap(0)
        return (min_element._key,min_element._value)

    def length(self):
        """ Return the number of items in the heap. """
        return len(self._heap)
    
    def update_key(self, element, newkey):
        i = element._index
        self._heap[i]._key = newkey
        self._rebalance(i)
        
    def get_key(self, element):
        return element._key

    def remove(self,element):
        i = element._index
        self._heap[i]._wipe()
        self._heap[i] = self._heap[self.length()-1]
        self._heap[i]._index = i
        self._heap.pop()
        self._rebalance(i)
        return (element._key, element._value)

    def _rebalance(self, posn):
        if self._heap[self._parent(posn)] > self._heap[posn]:
            self._upheap(posn)
        smallest_child = self._smallestchild(posn)
        if smallest_child:
            if self._heap[smallest_child] < self._heap[posn]:
                self._downheap(posn)
    #
    # Now, the methods needed for the underlying heap implementation
    # These are designated 'private', with the leading underscore, since
    # client code should not have access to these - all access to the PQ
    # is meant to be via the standard 4 methods
    # You don't need to implement these if they are
    # not used in your 4 standard methods above, but
    # I find them useful.

    def _left(self, posn):
        """ Return the index of the left child of elt at index posn. """
        return 2*posn+1

    def _right(self, posn):
        """ Return the index of the right child of elt at index posn. """
        return 2*posn+2

    def _parent(self, posn):
        """ Return the index of the parent of elt at index posn. """
        return (posn-1)//2

    def _upheap(self, posn):
        """ Bubble the item in posn in the heap up to its correct place. """
        while self._heap[posn] < self._heap[self._parent(posn)] and self._parent(posn) >= 0:
            self._heap[posn], self._heap[self._parent(posn)] = self._heap[self._parent(posn)], self._heap[posn]
            self._heap[posn]._index = posn
            self._heap[self._parent(posn)]._index = self._parent(posn)
            posn = self._parent(posn)


    def _downheap(self, posn):
        """ Bubble the item in posn in the heap down to its correct place. """
        child_pos = self._smallestchild(posn)
        if child_pos is None:
            return

        while self._heap[posn] > self._heap[child_pos]:
            self._heap[posn], self._heap[child_pos] = self._heap[child_pos], self._heap[posn]
            self._heap[posn]._index = posn
            self._heap[child_pos]._index = child_pos
            posn = child_pos
            child_pos = self._smallestchild(posn)
            if child_pos is None:
                break
    
    def _smallestchild(self, posn):
        # no child
        left, right = self._left(posn), self._right(posn)
        if left > self.length()-1:
            return None
        # only left child
        if left == self.length()-1:
            return self._left(posn)
        # both children
        if self._heap[left] < self._heap[right]:
            return left
        return right

    def _printstructure(self):
        """ Print out the elements one to a line. """
        for elt in self._heap:
            if elt is not None:
                print('(', elt._key, ',', elt._value, ')')
            else:
                print('*')

class TestAPQ():

    def testadd(self):
        print('Testing that we can add items to an array-based binary heap PQ')
        pq = APQBinaryHeap()
        print('pq has size:', pq.length(), '(should be 0)')
        pq.add(25,'25')
        pq.add(4, '4')
        print('pq has size:', pq.length(), '(should be 2)')
        print(pq, '(should be 4,25, could also show index and value)')
        pq.add(19,'19')
        pq.add(12,'12')
        print(pq, '(should be 4,12,19,25)')
        pq.add(17,'17')
        pq.add(8,'8')
        print(pq, '(should be 4,12,8,25,17,19)')
        print('pq length:', pq.length(), '(should be 6)')
        print('pq min item:', pq.min(), '(should be 4)')
        print()
        return pq

    def test(self):
        print('Testing that we can add and remove items from an array-based binary heap PQ')
        pq = APQBinaryHeap()
        print('pq has size:', pq.length())
        loc = {}
        print('Adding ant with value 25')
        loc['ant'] = pq.add(25,'ant')
        print('pq has size:', pq.length())
        print(pq)
        print('Adding bed with value 4')
        loc['bed'] = pq.add(4, 'bed')
        print(pq)
        print('Adding cat with value 14')
        loc['cat'] = pq.add(14,'cat')
        print(pq)
        print('Adding dog with value 12')
        loc['dog'] = pq.add(12,'dog')
        print(pq)
        print('Removing first')
        min = pq.remove_min()
        print("Just removed", str(min))
        print(pq)
        print('Adding egg with value 17')
        loc['egg'] = pq.add(17,'egg')
        print(pq)
        print('Adding fox with value 8')
        loc['fox'] = pq.add(8,'fox')
        print(pq)
        print('pq length:', pq.length())
        print('pq min item:', pq.min())
        for i in range(pq.length()):
            key, value = pq.remove_min()
            print('removed min (', key, value, '):', pq)

    def testaddAPQ(self):
        print('Testing that we can add items to an array-based binary heap PQ')
        pq = APQBinaryHeap()
        print('pq has size:', pq.length(), '(should be 0)')
        pq.add(25,'25')
        pq.add(4, '4')
        print('pq has size:', pq.length(), '(should be 2)')
        print(pq, '(should be 4,25, could also show index and value)')
        pq.add(19,'19')
        pq.add(12,'12')
        print(pq, '(should be 4,12,19,25)')
        pq.add(17,'17')
        pq.add(8,'8')
        print(pq, '(should be 4,12,8,25,17,19)')
        print('pq length:', pq.length(), '(should be 6)')
        print('pq min item:', pq.min(), '(should be 4)')
        print()
        return pq
    
    def testupdateAPQ(self):
        print('Testing that we can add items to an array-based binary heap PQ')
        pq = APQBinaryHeap()
        print('pq has size:', pq.length(), '(should be 0)')
        e25 = pq.add(25,'25')
        e4 = pq.add(4, '4')
        print('pq has size:', pq.length(), '(should be 2)')
        print(pq, '(should be 4,25, could also show index and value)')
        e19 = pq.add(19,'19')
        e12 = pq.add(12,'12')
        print(pq, '(should be 4,12,19,25)')
        e17 = pq.add(17,'17')
        e8 = pq.add(8,'8')
        print(pq, '(should be 4,12,8,25,17,19)')
        print('pq length:', pq.length(), '(should be 6)')
        print('pq min item:', pq.min(), '(should be 4)')
        pq.update_key(e12, 2)
        print(pq, "(should be 2,...)")
        pq.update_key(e4, 50)
        print(pq, " (should be 2, ..., 50)")
        pq.remove(e25)
        print(pq, "should remove 25")
        print()
        return pq

if __name__ == "__main__":
    bh = TestAPQ()
    bh.testaddAPQ()
    bh.test()
    bh.testupdateAPQ()