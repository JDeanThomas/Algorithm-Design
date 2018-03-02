# Karker's algorithm to compute minimum cuts in an adjecency graph (multithreaded)

# ReadAdjGraph takes an adjacency graph from text file where the first element 
# in each line represents a node and all subsequent values in the line represents 
# an edge. Returns graph as a dictionary object that represents an adjaceny graph
from readData import readAdjGraph
import random


random.seed(11)

def kargerMinCut(graph):
    cuts = []
    while len(graph) > 2:
        n = random.choice(list(graph.keys()))
        v = random.choice(graph[n])
        contract(graph, n, v) 
    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)
    print("MinCut is " + str(min(cuts)))

def contract(graph, n, v):
    for node in graph[v]:
        if node != n:
            graph[n].append(node)
        graph[node].remove(v)
        if node != n:
            graph[node].append(n)
    del graph[v]
    

def main():
    graph = kargerMinCut(readAdjGraph("data/kargerMinCut.txt"))
    print graph

if __name__ == '__main__':
    main()

