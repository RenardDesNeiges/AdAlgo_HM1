#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys
import heapq

def addToDeltas(delta, id):
    flag = False
    for el in delta:
        if el[1] == id:
            el[0] = el[0] + 1
            flag = True
            break
    if flag == False:
        delta.append([1,id])

def turbo_greddy(deltas,edges,n):
    cost = 0
    while deltas[0][0] > 1:
        # print(deltas)
        (v, vid) = heapq._heappop_max(deltas)
        cost = cost + 2
        # print("v : " + str(v) + " ; id : " + str(id))
        t = 0
        if(vid > n):
            t  = 1
            
        # print("VID = " + str(vid))
        for e in edges:
            if(e[t] == vid):

                did = e[1]
                if t==1 :
                    did = e[0]
                # print(e)
                # print("DID = " + str(did))
                for i in range(len(deltas)):
                    # print(deltas[i])
                    # print(deltas[i])
                    if(deltas[i][1] == did):
                        # print("decreasing "+str(i))
                        deltas[i][0] = deltas[i][0] - 1
                        heapq._siftdown_max(deltas,i,i)
        # heapq._heapify_max(deltas)

    # print(deltas)
    cost = cost + sum(d for d, _ in deltas)/2
    return int(cost)


lnb = 0

n = 0 #number of bridgeports
m = 0 #number of bridges

edges = []
deltas = []

# parse the input buffer and create the edge and delta lists
for line in sys.stdin:
    lst = line.split(' ')
    if lnb == 0:
        n = int(lst[0])
        m = int(lst[1])
    else:
        edges.append((int(lst[0]),int(lst[1]) + n))
        addToDeltas(deltas,int(lst[0]))
        addToDeltas(deltas,int(lst[1])+n)

    lnb = lnb + 1

#for good performance we need delta to be a maxheap so let's heapify it
heapq._heapify_max(deltas)

print(turbo_greddy(deltas,edges,n))