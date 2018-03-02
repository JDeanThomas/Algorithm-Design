# Functions for reading in data structures from plain text

from collections import defaultdict

# Read in numerical array

def readArray(filename):   
    array = []
    with open(filename, "r") as f:
        for val in f.read().split():
            array.append(int(val))
    return array  


# Takes a graph from text file where the first element in each line represents
# a vertex and all subsequent values in the line represents and edge. 
# Returns graph as a dictionary object that represents an adjaceny graph
	
def readAdjGraph(filename):
    graph = {}
    with open(filename) as file:
        for line in file:
            vertex, edges = int(line.split()[0]), line.split()[1:]          
            graph[vertex] = edges
    print(str(len(graph)) + " vertices in dictionary.")
    return graph
    
    
# Graphs from ajaceny lists. First column is vertext (repeated) 2nd is edge
# For files that omit column entry that have vertexts that exsist (pointed to)
# but do not have column in entry (point to no other vertextes)

# Read undirected graph. Ordered.
def readGraph(filename):
    graph = {}
    nextKey = 0
    with open(filename) as f: 
        for line in f:
            nextKey += 1
            items = [int(val) for val in line.split()]
            key, values = int(items[0]), items[1:]
            if key > nextKey:
                while key > nextKey:
                    graph[nextKey] = []
                    nextKey += 1
            graph.setdefault(key, []).extend(values)
            nextKey = key
    return graph
    
# Read directed graph into defaultdict. Unordered.    
def readDirectedGraph(filename):
    graph = defaultdict(list)
    with open(filename) as f: 
        for line in f:
            vertex, edge = line.strip().split()
            graph[vertex].append(edge)
    return graph
    
# Can reverse either of above directed graphs. Returns regular dict.    
def reverseGraph(graph):
    revGraph = defaultdict(list)
    for vertex in graph:
        for edge in graph[vertex]:
            revGraph[edge].append(vertex)
    return dict(revGraph)
    
# Can reverse either of above directed graphs. Returns regular defaultdict.    
def reverseGraphDefault(graph):
    revGraph = defaultdict(list)
    for vertex in graph:
        for edge in graph[vertex]:
            revGraph[edge].append(vertex)
    return revGraph



