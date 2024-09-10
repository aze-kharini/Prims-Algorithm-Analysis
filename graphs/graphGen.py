import random
from graphADT import Graph
from math import sqrt, ceil, log2

class GraphGen(object):

    def __init__(self):
        self.graph = Graph()
        self.full_conns = []
        self.span_conns = set()
        self.full_span_stepper = 0
        self.vertices = []
        self.edge_counter = 0
        self.max_weight = 3

    def __str__(self):
        printStr = "Full edges:\n%s\n\nSpanning edges:\n%s\n\nFull edges stepper at index: %d\nElement at index: %s\nEdges in graph: %d\n"%(str(self.full_conns), str(self.span_conns), self.full_span_stepper, str(self.full_conns[self.full_span_stepper]), self.edge_counter)
        return printStr
    
    def reset(self):
        self.graph = Graph()
        self.full_conns = []
        self.span_conns = set()
        self.full_span_stepper = 0
        self.vertices = []
        self.edge_counter = 0

    def genGraph(self, n, m):
        if m<n-1 or m>n*(n-1)//2:
            return None
        return self._genDenseGraphAddition(n, m)
    
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
# Generation of a dense graph by generating all posible pairings and shuffling them

    def _genFullGraphConnections(self, n):
        conns = []
        for i in range(n-1):
            for j in range(i+1, n):
                conns.append((i, j))
        random.shuffle(conns)
        return conns
    
    def _genMinGraphConnectionsInduction(self, n):
        conns = []
        path = list(range(n))
        random.shuffle(path)
        conns.append((path[0], path[1]))
        for i in range(2,n):
            conns.append((path[self._pickRandomElementIterative(i)-1], path[i]))
        random.shuffle(conns)
        return conns
    
    def _pickRandomElementIterative(self, n):
        x = random.randint(1, 2*n-1)
        if x < n:
            return x
        return n

    def _genDenseGraphAddition(self, n, m):
        self.reset()
        self.graph = Graph()
        self.vertices = []
        for i in range(n):
            self.vertices.append(self.graph.add_vertex(i))
        minConns = self._genMinGraphConnectionsInduction(n)
        self.span_conns = set(minConns)
        self.edge_counter = 0
        for conn in minConns:
            self.graph.add_edge(self.vertices[conn[0]], self.vertices[conn[1]], self.edge_counter, random.randint(1, 20))
            self.edge_counter += 1
        self.full_conns = self._genFullGraphConnections(n)
        self.full_span_stepper = 0
        self.addEdges(m)

    def addEdges(self, m):
        n = len(self.vertices)
        if self.edge_counter > m:
            raise Exception("Desired number of edges is lower than the current number of adges, cannot add")
        if m > n*(n-1)//2:
            raise Exception("Impossible number of edges")
        while self.edge_counter < m:
            conn = self.full_conns[self.full_span_stepper]
            weight = self.genWeight()
            while self.graph.add_edge(self.vertices[conn[0]], self.vertices[conn[1]], self.edge_counter, weight) is None:
                self.full_span_stepper += 1
                conn = self.full_conns[self.full_span_stepper]
            self.edge_counter += 1

    def removeEdges(self, m):
        n = len(self.vertices)
        if self.edge_counter <= m:
            raise Exception("Desired number of edges is higher than the current number of adges, cannot remove")
        if m < n-1:
            raise Exception("Impossible number of edges")
        while self.edge_counter > m:
            conn = self.full_conns[self.full_span_stepper]
            while set((conn)).issubset(self.span_conns):
                self.full_span_stepper -= 1
                conn = self.full_conns[self.full_span_stepper]
            assert self.graph.remove_edge(self.vertices[conn[0]], self.vertices[conn[1]]) is not None
            self.edge_counter -= 1
            self.full_span_stepper -= 1
            
    def genWeight(self):
        return random.randint(1,self.max_weight)
    
def calculate_c(n, m, w):
    d = m/n
    # print("average checks per vertex: "+ str(d))
    # x=w*(2*w**(d-1)-1)
    # print("number of different elements in each set added up: "+str(x))
    # print("number of sets is: " + str(w**d))
    # s =(x/(w**(d)))*w
    # print("average number of different costs on a vertex: " + str(s))
    # print(bin_divide(s))
    c = (log2(min(w, d)+1/2)/(d))*m
    return c

def eval_c(n, w):
    gen = GraphGen()
    n = 100
    gen.max_weight = w
    with open("c_testing.txt", "w") as toFile:
        for i in range(n, n*(n-1)//2, n):
            m = i
            # c_sum = 0
            # c_tries = 0
            cost_sum = 0
            cost_count = 0
            checks_count = 0
            updates_count = 0
            tests = 20
            for i in range(tests):
                gen.genGraph(n, m)
                tree, updates, checks, cost_sum_1,cost_count_1 = gen.graph.primData("heap")
                cost_count += cost_count_1
                cost_sum += cost_sum_1
                checks_count += checks
                updates_count += updates

            # real_c = (updates_count/checks_count)
            # real_s = cost_sum/cost_count
            # print("average number of real updates: " + str(updates_count/tests), str(m))
            toFile.write("%10d\t%10.2f\n"%(m, updates_count/checks_count))

if __name__ == "__main__":
    eval_c(100, 20)