from APQUnsortedList import APQUnsortedList
from APQBinaryHeap import APQBinaryHeap

class TestAPQ():

    def __init__(self, APQ):
        self._apq = APQ

    def getAPQ(self):
        return self._apq
    
    def setAPQ(self, apq):
        self._apq = apq
    
    apq = property(getAPQ, setAPQ)

    def testadd(self):
        print('Testing that we can add items to an array-based binary heap PQ')
        pq = self.apq()
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
        pq = self.apq()
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
        pq = self.apq()
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
        pq = self.apq()
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
    test = TestAPQ(APQUnsortedList)
    test.testadd()
    test.test()
    test.testupdateAPQ()
    test.testaddAPQ()
