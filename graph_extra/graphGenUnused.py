import random
# from graphs/graphADT import Graph
from math import sqrt, ceil

class GraphGen(object):

    def genGraph(self, n, m): #m>=n
        if m<n-1 or m>n*(n-1)//2:
            return None
        elif m<n*(n-1)//4:
            return self._genSparseGraph(n, m)
        return self._genDenseGraph(n, m)
    
####################################
# Index Utils

    def _get_random_index(self, i, n):
        if i == 0:
            return random.randint(1, n)
        if i==n:
            return random.randint(0,n-1)
        return random.choice([random.randint(0, i-1), random.randint(i+1, n)])
    
    def _genRadnomIndexes(self,n):
        return (random.randint(0, n-1),random.randint(0, n-1))

    def _rollIndexes(self, indexes, n):
        i1, i2 = indexes
        i1 = (i1+1)%n
        if i1==0:
            i2 = (i2+1)%n
        return i1, i2

####################################
# Generation of a graph by random picking of vertices to add

    def _genSparseGraph(self, n, m):
        graph, vertices = self._genMinGraph(n)
        self._addEdges(graph, vertices, m-(n-1))
        return graph
    
    def _addEdges(self, graph, vertices, x):
        n = graph.num_vertices()
        for i in range(x):
            weight = random.randint(1, 20)
            i1, i2 = self._genRadnomIndexes(n)
            while True:
                if graph.add_edge(vertices[i1], vertices[i2], i+(n-1), weight): # O(1) test if edge exists
                    break
                # i1, i2 = self._rollIndexes([i1, i2], n)
                i1, i2 = self._genRadnomIndexes(n)

    def _genMinGraph(self, n):
        graph = Graph()
        vertices = []
        for i in range(n):
            vertices.append(graph.add_vertex(i))
        self._addRandomSkeleton(graph, vertices)

        return graph, vertices
    
    def _addRandomSkeleton(self, graph, vertices):
        n = graph.num_vertices()
        chain = list(range(n))
        random.shuffle(chain)
        for i in range(1, n):
            graph.add_edge(vertices[chain[i-1]], vertices[chain[i]], i, random.randint(1, 20))
    
####################################
# Generation of a graph by random picking of vertices to remove

    def _genDenseGraphRemoval(self, n ,m):
        graph, vertices = self._genFullGraph(n)
        skeleton = self._randomSkeleton(graph, vertices)
        self._removeEdges(graph, skeleton, vertices, n*(n-1)//2-m)
        return graph
    
    def _removeEdges(self, graph, notRemove, vertices, x):
        n = graph.num_vertices()
        for _ in range(x): # number of edges to be removed                
            i1, i2 = self._genRadnomIndexes(n)
            while True: 
                while {graph.get_edge(vertices[i1], vertices[i2])}.issubset(notRemove): # do not touch the skeleton
                    i1, i2 = self._genRadnomIndexes(n)
                    # i1, i2 = self._rollIndexes([i1, i2], n)  
                if graph.remove_edge(vertices[i1], vertices[i2]): # edge could already be removed
                    break
                i1, i2 = self._genRadnomIndexes(n)
                # i1, i2 = self._rollIndexes([i1, i2], n)
    
    def _genFullGraph(self, n):
        graph = Graph()
        vertices = [graph.add_vertex(0)]
        counter = 0
        notRemoveEdges = set()
        for i in range(1,n):
            vertices.append(graph.add_vertex(i))
            notRemoveEdges.add(graph.add_edge(vertices[i], vertices[0], counter, random.randint(1, 20)))
            counter+=1
        for i in range(1, n-1):
            for j in range(i+1, n):
                graph.add_edge(vertices[i], vertices[j], counter, random.randint(1, 20))
                counter +=1 
        # print(str(counter), "should equal to", str(n*(n-1)//2))
        return graph, vertices

    def _randomSkeleton(self, graph, vertices):
        n = graph.num_vertices()
        skeleton = set()
        chain = list(range(n))
        random.shuffle(chain)
        for i in range(1, n):
            skeleton.add(graph.get_edge(vertices[chain[i-1]], vertices[chain[i]]))
        return skeleton
    
####################################
# Generation of a graph by generating all posible pairings and shuffling them

    def _genFullGraphConnections(self, n):
        conns = []
        counter = 0
        for i in range(n-1):
            for j in range(i+1, n):
                conns.append((i, j))
                counter += 1
        random.shuffle(conns)
        return conns

    def _genMinGraphConnectionsChain(self, n):
        conns = []
        vertices = list(range(n))
        random.shuffle(vertices)
        for i in range(1,n):
            conns.append((vertices[i-1], vertices[i]))
        random.shuffle(conns)
        # chain of connections
        # shuffle the chain around

        return conns
    
    def _genMinGraphConnectionsInduction(self, n):
        conns = []
        vertices = list(range(n))
        random.shuffle(vertices)
        print(vertices)
        conns.append((vertices[0], vertices[1]))
        for i in range(2,n):
            conns.append((vertices[self.pickRandomElementIterative(i)-1], vertices[i]))
        random.shuffle(conns)
        return conns
    
    def pickRandomElementIncreasingDistribution(self, n):
        range = n*(n+1)//2
        x = random.randint(1, range)
        element = ceil((-1+sqrt(1+8*x))/2)
        # for i in range(100):
        #     print(ceil((-1+sqrt(1+8*i))/2))
        return element
    
    def pickRandomElementIterative(self, n):
        x = random.randint(1, 2*n-1)
        if x < n:
            return x
        return n
    


    def _genDenseGraphAddition(self, n, m):
        graph = Graph()
        vertices = []
        for i in range(n):
            vertices.append(graph.add_vertex(i))
        minConns = self._genMinGraphConnectionsInduction(n)
        counter = 0
        for conn in minConns:
            graph.add_edge(vertices[conn[0]], vertices[conn[1]], counter, random.randint(1, 20))
            counter += 1
        allConns = self._genFullGraphConnections(n)
        i = 0
        while counter < m:
            conn = allConns[i]
            weight = random.randint(1, 20)
            while graph.add_edge(vertices[conn[0]], vertices[conn[1]], counter, weight) is None:
                i += 1
                conn = allConns[i]
            counter += 1
        return graph
    
if __name__ == "__main__":
    gen = GraphGen()
    # print(gen.genGraph(100, 2500))
    # print(random.randint(0,0))
    # print(gen._genFullGraphConnections(4))
    # print(gen._genDenseGraphAddition(4, 6))
    print(gen._genDenseGraphAddition(4, 3))
    # print(gen.pickRandomElementIncreasingDistribution(5))