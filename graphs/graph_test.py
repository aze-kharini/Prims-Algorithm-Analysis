from graphADT import *
from graphGen import GraphGen

class TestGraph():

    def __init__(self):
        self.graph = Graph()
    
    def test_small(self):
        self.graph = Graph()
        self.graph.add_vertex("x")
        self.graph.add_vertex("y")
        self.graph.add_vertex("z")
        self.graph.add_edge(Vertex("x"), Vertex("y"), "e")
        self.graph.add_edge(Vertex("y"), Vertex("z"), "f")
        print(self.graph)

    def test_states(self):
        self.graph = Graph()
        toFile = open("contiguous-usa.dat", "r")
        lines = toFile.readlines()
        toFile.close()
        for line in lines:
            states = line.strip().split(" ")
            self.graph.add_vertex(states[0])
            self.graph.add_vertex(states[1])
        for i, line in enumerate(lines):
            states = line.strip().split(" ")
            self.graph.add_edge(Vertex(states[0]), Vertex(states[1]), i)
        
        maxBorders = 0
        maxBordersState = ""
        for state in self.graph.vertices():
            if self.graph.degree(state) > maxBorders:
                maxBorders = self.graph.degree(state)
                maxBordersState = state
        print(str(maxBordersState), str(maxBorders))
        
        print(self.graph)

        print(self.graph.central_vertex())

    def test_dolphins(self):
        self.graph = Graph()
        toFile = open("dolphins.gml", "r")
        lines = toFile.readlines()
        toFile.close()
        lines = lines[4:-1]
        dolphins = {}
        for i in range(len(lines)):
            if "[" in lines[i] and "id" in lines[i+1]:
                dolphins[int(lines[i+1].strip("id \n"))] = lines[i+2].strip("label \"\n")
        for dolphin_id in dolphins:
            self.graph.add_vertex(dolphin_id)
        id_counter = 0
        for i in range(len(lines)):
            if "[" in lines[i] and "source" in lines[i+1]:
                source = int(lines[i+1].strip("source \n"))
                target = int(lines[i+2].strip("target \n"))
                self.graph.add_edge(Vertex(source), Vertex(target), id_counter)
                id_counter += 1
        print(self.graph)

        maxConns = 0
        social_dolphin = -1
        for dolphin in self.graph.vertices():
            if self.graph.degree(dolphin) > maxConns:
                maxConns = self.graph.degree(dolphin)
                social_dolphin = dolphin
        print(str(social_dolphin), str(dolphins[social_dolphin.element]), str(maxConns))

        print("Depth frist search: ")
        dfs = self.graph.DFS(Vertex(1))
        for item in dfs.items():
            print(item)
        print("\nCount: " + str(len(dfs)))

        
        print("\n\nBreadth first Search: ")
        bfs = self.graph.BFS(Vertex(1))
        for item in bfs.items():
            print(item)
        print("\nCount: " + str(len(bfs)))

        print("\n\nMax shortest path: " + str(self.graph.max_shortest_path(Vertex(1))))

        print("\n\nCentral Dolphin: " + dolphins[self.graph.central_vertex()[0].element], str(self.graph.central_vertex()[1]))

    def test_prim(self, n, m):
        gen = GraphGen()
        gen.genGraph(n, m)
        print("graph{")
        for e in gen.graph.edges():
            print("%s -- %s;"%(str(e.pair[0]), str(e.pair[1])), end="")

        tree = gen.graph.prim("heap")
        print()
        for e in tree:
            print("p%s -- p%s;"%(str(e.pair[0]), str(e.pair[1])), end="")
        print("}")




if __name__ == "__main__":
    test = TestGraph()
    test.test_prim(10, 10)