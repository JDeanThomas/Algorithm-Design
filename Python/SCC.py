### Kosaraju's algorithm for finding strongly connected components

from readData import readDirectedGraph, reverseGraph
from collections import defaultdict


def forward(graph):
    seen = set()
    ordering = []

    def dfs(v):
        seen.add(v)
        for u in graph[v]:
            if u not in seen:
                dfs(u)
        ordering.append(v)

    for u in graph.keys():
        if u not in seen:
            dfs(u)
    return ordering

def backward(graph, ordering):
    seen = set()
    leader = defaultdict(list)
    for u in reversed(ordering):
        if u not in seen:
            # Non recursive DFS using a stack
            seen.add(u)
            stack = [u]
            while stack:
                item = stack.pop()
                for v in graph[item]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
                leader[u].append(item)
    return leader



def kosaraju(graph):
    return backward(graph, forward(reverseGraph(graph)))
    #return backward(graph, forward(reverseGraph2(defaultdict(dict, graph))))

def main():
    graph = readDirectedGraph('Data/directedGraph.txt')
    #print graph
    # Store dict of Strongly Connected Components of graph
    sccs = kosaraju(graph).values()
    # Print 10 most strongly connected components of graph
    print sorted(map(len, sccs))[::-1][:10]
    

def test():
    graph = {
        1: [2],
        2: [3, 5],
        3: [4],
        4: [6],
        5: [1],
        6: [3]
    }
    print kosaraju(graph)

if __name__ == '__main__':
    from sys import setrecursionlimit
    setrecursionlimit(80000)
    main()
    #test()
