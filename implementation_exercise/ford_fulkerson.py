#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
# from collections import defaultdict

#find BFS path in the network
def BFS(net,n,trace):
    source = 0
    sink = 2*n+1

    queue = [] #no need for priority queue here, just first in first out ?(I think)?

    visited = [False] * (2*n+2)

    queue.append(source)
    visited[source] = True

    while queue:
        v = queue.pop(0)
        #get all unvisited successors (adj(v))
        for i, c in enumerate(net[v]):  # enumerate returns indices of iterator, more pythonic than a loop on a range
            if( not visited[i] and c > 0):
                trace[i] = v
                if i == sink:           # if we reached the sink, then BFS is finished, return True
                    visited[i] = True
                    return True
                else:                   # else we add the neighbor to the queue, it's a successor
                    queue.append(i)
                    visited[i] = True

    return False

#compute max flow in the network
def MaxFlox(net,n):
    source = 0
    sink = 2*n+1

    trace = [-1]*(2*n+2)

    flow = 0


    while BFS(net,n,trace):

        # find max path for given flow
        v = sink
        flow_along_path = sys.maxsize
        # additionnal flow along the augmenting path is the flow at the path's bottlneck
        # we find the bottleneck by going backwards along the trace of BFS

        while v != source:
            flow_along_path = min( flow_along_path , net[trace[v]][v] )
            v = trace[v]

        # decrease the capacitites along the path, go back the BFS trace
        v = sink
        while v != source:
            net[trace[v]][v] = net[trace[v]][v] - flow_along_path
            net[v][trace[v]] = net[v][trace[v]] + flow_along_path
            v = trace[v]

        # increase the total flow
        
        flow = flow + flow_along_path

    return flow

lnb = 0

n = 0 #number of bridgeports
m = 0 #number of bridges

edges = []
adjMat = []

# parse the input buffer and create the edge and delta lists
for line in sys.stdin:
    lst = line.split(' ')
    if lnb == 0:
        # get the graph dimensions, construct the empty adj matrix
        n = int(lst[0])
        m = int(lst[1])

        for i in range(2*n+2):          # We create a graph with 2n+2 vertices (1 per port + a source and a sink)
            adjMat.append([0]*(2*n+2))

        # connect every port to the source/sink with a vertex of capacity 2
        for i in range(n):
            adjMat[0][i+1] = 2
            adjMat[i+n+1][2*n+1] = 2

    else:
        e1 = int(lst[0])         # edge 0 is source
        e2 = int(lst[1]) + n     # edge 0 is source
        adjMat[e1][e2] = 1


    lnb = lnb + 1


# for y in range(2*n+2):
#     for x in range(2*n+2):
#         print(adjMat[y][x],end="")
#     print("")

print(MaxFlox(adjMat,n))
# print(adjMat)