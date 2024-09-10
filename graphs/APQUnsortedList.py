
class APQUnsortedList:
    """ Maintain an collection of items, popping by lowest key.
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
        self._list = []
        
    def __str__(self):
        """ Return a breadth-first string of the values. """
        string = ""
        for element in self._list:
            string += str(element._key) + ":" + str(element._value) + "["+str(element._index)+"]" + ", "
        return string
    
    def __repr__(self):
        return self.__str__()
            
    def add(self, key, value):
        """ Add Element(key,value) """
        new_element = self.Element(key,value, self.length()) # for appending it
        self._list.append(new_element)
        return new_element

    def min(self):
        """ Return the min priority key,value. """
        if self.length() > 0:
            min_element = self._list[0]
            for element in self._list[1:]:
                min_element = min(min_element, element)
            return min_element
        return None

    def remove_min(self):
        """ Remove and return the min priority key,value. """
        if self.length() > 0:
            min_element = self.min()
            self._list[min_element._index] = self._list[self.length()-1]
            self._list[min_element._index]._index = min_element._index
            self._list.pop()
            return (min_element._key,min_element._value)
        return None

    def length(self):
        """ Return the number of items """
        return len(self._list)
    
    def update_key(self, element, newkey):
        self._list[element._index]._key = newkey
        
    def get_key(self, element):
        return element._key

    def remove(self,element):
        i = element._index
        self._list[i]._wipe()
        self._list[i] = self._list[self.length()-1]
        self._list[i]._index = i
        self._list.pop()
        return (element._key, element._value)