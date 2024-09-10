from APQBinaryHeap import APQBinaryHeap
from APQUnsortedList import APQUnsortedList

class Vertex(object):

    def __init__(self, element):
        self._element = element
    
    def getElement(self):
        return self._element
    
    def setElement(self, element):
        self._element = element

    element = property(getElement, setElement)

    def __str__(self):
        return str(self.element)
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.element == other.element:
            return True
        return False
    
    def __hash__(self):
        return hash(self.element)
    

class Edge(object):

    def __init__(self, x, y, label, weight=None):
        self._pair = [x,y]
        self._label = label
        self._weight = weight
    
    def getPair(self):
        return self._pair
    
    def setPair(self, pair):
        self._pair = pair

    def getLabel(self):
        return self._label
    
    def setLabel(self, label):
        self._label = label

    def getWeight(self):
        return self._weight
    
    def setWeight(self, weight):
        self._weight = weight

    pair = property(getPair, setPair)
    label = property(getLabel, setLabel)
    weight = property(getWeight, setWeight)

    def __str__(self):
        return str(self.label)+str(self.pair)+str(self.weight)
    
    def __repr__(self):
        return self.__str__()

    def vertices(self):
        return self.pair
    
    def opposite(self, x):
        if self.pair[0] == x:
            return self.pair[1]
        return self.pair[0]
    
    def element(self):
        return self.label
    
    def first(self):
        return self.pair[0]
    
    def second(self):
        return self.pair[1]
    
class Graph(object):

    def __init__(self):
        self._vertices = {}

    def vertices(self):
        return self._vertices.keys()
    
    def __str__(self):
        print_str = ""
        for item in self._vertices.items():
            print_str += str(item) + "\n"
        return print_str
    
    def __repr__(self):
        return self.__str__()
            
    def edges(self):
        edges = set()
        for connections in self._vertices.values():
            for edge in connections.values():
                edges.add(edge)
                # if edge not in edges:
                #     edges.append(edge)
        return list(edges)
    
    def num_vertices(self):
        return len(self._vertices)
    
    def num_edges(self):
        return len(self.edges())
    
    def get_edge(self, x, y):
        edge = None
        conns = self._vertices.get(x)
        if conns:
            edge = conns.get(y)
        return edge
    
    def degree(self,x):
        return len(self._vertices.get(x, {}))
    
    def get_edges(self, x):
        conns = self._vertices.get(x, {})
        return conns.values()

    def add_vertex(self, elt):
        new_vertex = Vertex(elt)
        if self._vertices.get(new_vertex) is None:
            self._vertices[new_vertex] = {}
            return new_vertex
        return None

    def add_edge(self, x, y, elt, weight=None):
        if x != y and self.get_edge(x,y) is None:
            new_edge = Edge(x, y, elt, weight)
            self._vertices.get(x)[y] = new_edge
            self._vertices.get(y)[x] = new_edge
            return new_edge
        return None

    def remove_vertex(self, vertex):
        connected = self._vertices.get(vertex, {}).keys()
        self._vertices.pop(vertex)
        for v in connected:
            v_conns = self._vertices[v]
            v_conns.pop(vertex)

    def remove_edge(self, x, y):
        x_conns = self._vertices.get(x)
        y_conns = self._vertices.get(y)
        if x_conns and y_conns:
            if x_conns.get(y) and y_conns.get(x):
                x_conns.pop(y)
                return y_conns.pop(x)
        return None

    def DFS(self, vertex):
        record = {vertex:"start"}
        self._dfs(vertex, record)
        return record
    
    def _dfs(self, vertex, record):
        for edge in self.get_edges(vertex):
            opposite_vertex = edge.opposite(vertex)
            if record.get(opposite_vertex) is None:
                record[opposite_vertex] = edge
                self._dfs(opposite_vertex, record)

    def BFS(self, vertex):
        record = {vertex: ("start", 0)}
        self._bfs([vertex], record, 1)
        return record
    
    def _bfs(self, layer_list, record, layer):
        new_layer_list = []
        for vertex in layer_list:
            for edge in self.get_edges(vertex):
                opposite_vertex = edge.opposite(vertex)
                if record.get(opposite_vertex) is None:
                    new_layer_list.append(opposite_vertex)
                    record[opposite_vertex] = (edge, layer)
        if len(new_layer_list) > 0:
            self._bfs(new_layer_list, record, layer+1)

    def max_shortest_path(self, vertex):
        record = {vertex: ("start", 0)}
        return self._msp([vertex], record, 1)
    
    def _msp(self, layer_list, record, layer):
        new_layer_list = []
        for vertex in layer_list:
            for edge in self.get_edges(vertex):
                opposite_vertex = edge.opposite(vertex)
                if record.get(opposite_vertex) is None:
                    new_layer_list.append(opposite_vertex)
                    record[opposite_vertex] = (edge, layer)
        if len(new_layer_list) > 0:
            return self._msp(new_layer_list, record, layer+1)
        else:
            return layer -1

    def central_vertex(self):
        central = (None, len(self.vertices())+1)
        for vertex in self.vertices():
            path = self.max_shortest_path(vertex)
            if central[1] > path:
                central = (vertex, path)
        return central
    
    def prim(self, APQ_type):
        pq = APQUnsortedList()
        if APQ_type == "heap":
            pq = APQBinaryHeap()
        locs = {}
        for vertex in self.vertices():
            element = pq.add(float("inf"), (vertex, None))
            locs[vertex] = element
        tree = []
        while pq.length() > 0:
            value = pq.remove_min()[1]
            vertex, entry_edge = value
            locs.pop(vertex)
            if entry_edge:
                tree.append(entry_edge)
            for edge in self.get_edges(vertex):
                opposite_vertex = edge.opposite(vertex)
                if locs.get(opposite_vertex):
                    cost = edge.weight
                    element = locs[opposite_vertex]
                    if cost < pq.get_key(element):
                        element.value = (opposite_vertex, edge)
                        pq.update_key(element, cost)
        return tree
    
    def primData(self, APQ_type):
        pq = APQUnsortedList()
        if APQ_type == "heap":
            pq = APQBinaryHeap()
        locs = {}
        for vertex in self.vertices():
            element = pq.add(float("inf"), (vertex, None))
            locs[vertex] = element
        tree = []
        checks = 0
        updates = 0
        cost_sum = 0
        cost_count = 0
        while pq.length() > 0:
            value = pq.remove_min()[1]
            vertex, entry_edge = value
            locs.pop(vertex)
            if entry_edge:
                tree.append(entry_edge)
            cost_set = set()
            for edge in self.get_edges(vertex):
                opposite_vertex = edge.opposite(vertex)
                if locs.get(opposite_vertex):
                    cost = edge.weight
                    cost_set.add(cost)
                    element = locs[opposite_vertex]
                    checks += 1
                    if cost < pq.get_key(element):
                        updates += 1
                        element.value = (opposite_vertex, edge)
                        pq.update_key(element, cost)
            if len(cost_set)>0:
                cost_count += 1
            cost_sum += len(cost_set)
        return tree, updates,checks, cost_sum,cost_count
                    

if __name__ == "__main__":
    pass




    

