from math import log2
from graphEval import GraphEval

def mapRuntimes0(max_n, scale):
    with open("runtimeMap.txt", "w") as toFile:
        n_step = max(1,max_n//100)
        for n in range(2, max_n, n_step):
            line = "%4d: "%n + " "*(n-2)
            if scale == "none":
                step = 1
            elif scale == "constant":
                step = 2**9
            else:
                step = max(1, (n*(n-1)//2-(n-1))//(n-1))
            for e in range(n-1, n*(n-1)//2+1, step):
                heap_runtime = e*log2(n)
                list_runtime = n**2
                if heap_runtime< list_runtime:
                    line += "."
                else:
                    line += "#"
            toFile.write(line+"\n")


def mapRuntimes(max_n, scale):
    with open("runtimeMap.txt", "w") as toFile:
        n_step = max(1,max_n//100)
        for n in range(2, max_n, n_step):
            line = "%d: "%n + " "*(n-2)
            if scale == "none":
                step = 1
            elif scale == "constant":
                step = max_n//(2**3)
                print("Steppin by "+str(step))
            else:
                step = max(1, (n*(n-1)//2-(n-1))//(n-1))
            # graphEval = GraphEval("mid_point_results")
            # real_change = graphEval.find_change(n, max(1, n**2//1000))
            for e in range(n-1, n*(n-1)//2+1, step):
                # if e <= real_change and e + step > real_change:
                #     line += "#"
                if list_better(n, e):
                    line += "."
                else:
                    line += ":"
            toFile.write(line+"\n")

def list_better(n, e):
    heap_runtime = e*log2(n)+2*n*log2(n)
    list_runtime = n**2+n+e
    return list_runtime<heap_runtime


mapRuntimes0(500, "constant")
class change():
    def find_change(self, n, precision=None):
        m = self.theoretical_change(n)
        t_m = m
        # print("theoretical change point: " + str(t_m))
        self._graphGen.genGraph(n, m)
        heapRuntime, unsortedListRuntime = self.testGraph()
        consecutive_success = 10
        successes = 0
        resets = 0
        jump = 0
        direction = 1 # increasing
        max_m = n*(n-1)//2
        precision = (max_m//1000)
        heapRuntime, unsortedListRuntime = self.testGraph()
        edges = m
        while m > n-1 and m < max_m:
            print("%2d:10| %10d:%10d"%(consecutive_success, m, max_m))
            if heapRuntime > unsortedListRuntime:
                # correct result
                consecutive_success -= 1
            else:
                # wrong result
                consecutive_success = 5
                resets += 1
                if resets > 10:
                    # check if the last 
                    jump = (max_m-m)//2**(7+successes)
                    m = m + jump*direction
                    # direction = direction*(-1)
                    resets = 0

                    jump = True

            if consecutive_success <= 0:
                if successes > 3:
                    break
                successes += 1
                consecutive_success = 5
            m = m+precision*direction
            jump=0
            if edges < m:
                self._graphGen.addEdges(m)
            else:
                self._graphGen.removeEdges(m)
            edges = m
            heapRuntime, unsortedListRuntime = self.testGraph()


        print("theoretical change point: " + str(t_m))
        print("real change point: "+str(m))
        print("difference: " + str(abs(t_m-m)))

        return m

    def theoretical_change(self, n):
        return (n*(n-2*log2(n)+1))//(log2(n)-1)
