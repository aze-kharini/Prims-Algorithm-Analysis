import time
from random import randint
from sort import heapsort, quicksort, mergesort, insertionsort
from copy import deepcopy

def shufflelist(inlist):
    n = len(inlist)
    for i in range(n):
        j = randint(0,n-1)
        inlist[i], inlist[j] = inlist[j], inlist[i]

def partialshufflelist(inlist, d):
    n = len(inlist)
    for i in range(n//d):
        j = randint(0,n-1)
        inlist[i], inlist[j] = inlist[j], inlist[i]

def randomlist(n, k):
    inlist = list(range(0,n-k))
    for i in range(k):
        inlist.append(inlist[randint(0, n-k-1)])
    shufflelist(inlist)
    return inlist

def testonealg(inlist, sortfunc):
    start_time = time.perf_counter()
    sortfunc(inlist)
    end_time = time.perf_counter()
    checksorted(inlist, sortfunc)
    return end_time - start_time

def checksorted(inlist, sortfunc):
    for i in range(len(inlist)-1):
        if inlist[i]>inlist[i+1]:
            print("Failed\nlist: " + str(inlist) + "\nError at " + str(i+1) + " index\nAlgorithm: " + sortfunc.__name__ )
            return

def evaluate(n, k, num, f):
    numlist = []
    oglist = randomlist(n, k)
    for i in range(num):
        copylist = deepcopy(oglist)
        shufflelist(copylist)
        numlist.append(copylist)
    sumtime = 0
    for inlist in numlist:
        sumtime += testonealg(inlist, f)
    avgtime = sumtime/num
    print("Algorithm: " + f.__name__ + "\tTime: " + str(avgtime) + "\tn=" + str(n) + "\tk=" + str(k))

def numlist(n,k,num):
    numlist = []
    oglist = randomlist(n, k)
    for i in range(num):
        copylist = deepcopy(oglist)
        shufflelist(copylist)
        numlist.append(copylist)
    return numlist

def partialnumlist(n,k,num,d):
    numlist = []
    oglist = randomlist(n, k)
    oglist.sort()
    for i in range(num):
        copylist = deepcopy(oglist)
        partialshufflelist(copylist, d)
        numlist.append(copylist)
    return numlist

def evaluateall(n,k,num,funcs):
    ognumlist = numlist(n,k,num)
    for f in funcs:
        if n<5000 or f.__name__ != "insertionsort":
            innumlist = deepcopy(ognumlist)
            sumtime = 0
            for inlist in innumlist:
                sumtime += testonealg(inlist, f)
            avgtime = sumtime/num
            print("Algorithm: " + f.__name__ + "\tTime: " + str(avgtime) + "\tn=" + str(n) + "\tk=" + str(k))

def evaluateallpartial(n,k,d,num,funcs):
    ognumlist = partialnumlist(n,k,num, d)
    for f in funcs:
        if n<5000 or f.__name__ != "insertionsort":
            innumlist = deepcopy(ognumlist)
            sumtime = 0
            for inlist in innumlist:
                sumtime += testonealg(inlist, f)
            avgtime = sumtime/num
            print("Algorithm: " + f.__name__ + "\tTime: " + str(avgtime) + "\tn=" + str(n) + "\tk=" + str(k))


def evalautescale():
    parameters = [(100, 20),
                  (1000, 200),
                  (10000, 2000),
                  (100000, 20000),
                  (1000000, 200000)]
    functions = [quicksort, mergesort, heapsort, insertionsort]
    for (n,k) in parameters:
        print("random:")
        evaluateall(n,k,20,functions)
        print("partially sorted: ")
        evaluateallpartial(n,k,n//100, 20, functions)

if __name__=="__main__":
    evalautescale()


