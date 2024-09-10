from graphGen import GraphGen
import time
from math import log2

class GraphEval():

    def __init__(self, fileName):
        self._report_file = fileName
        with open(self._report_file, "w") as toFile:
            toFile.write("")
        self._graphGen = GraphGen()
        self.results = []
    
    def _writeToFile(self,n, m, heapRuntime, unsortedListRuntime):
        with open(self._report_file, "a") as toFile:
            # line = "Vertices=%6d\tEdges=%6d\tHeap=%10.8f\tUnsorted List=%10.8f\n" % (n, m, heapRuntime, unsortedListRuntime)
            line = "%10d\t%d\t%12.8f\t%12.8f\n" % (n, m, heapRuntime, unsortedListRuntime)
            toFile.write(line)
    
    def testGraph(self):
        startTime = time.time()
        tree = self._graphGen.graph.prim("heap")
        endTime = time.time()
        assert self._graphGen.graph.num_vertices()-1 == len(tree)
        heapRuntime = endTime - startTime
        startTime = time.time()
        tree = self._graphGen.graph.prim("list")
        endTime = time.time()
        assert self._graphGen.graph.num_vertices()-1 == len(tree)
        unsortedListRuntime = endTime - startTime
        return (heapRuntime, unsortedListRuntime)
    
    def reportGraph(self,n,m):
        print("n="+str(n), "m="+str(m))
        self._graphGen.genGraph(n, m)
        heapRuntime, unsortedListRuntime = self.testGraph()
        self.results.append((n, m, heapRuntime, unsortedListRuntime))
        self._writeToFile(n, m, heapRuntime, unsortedListRuntime)

    def reportVertices(self, n, x):
        minE = n-1
        maxE = (n-1)*n//2
        step = (maxE-minE)//x
        diff = (maxE-minE)%x
        counter = minE
        for _ in range(x+1):
            self.reportGraph(n, counter)
            if diff>0:
                counter += 1
                diff -= 1
            counter += step
        
    def report(self, max_power):
        for i in range(8, max_power+1):
            self.reportVertices(2**i, 10)


if __name__ == "__main__":
    test = GraphEval("graph_results.txt")
    test.report(12)
