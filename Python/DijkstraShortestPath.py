# Distijkstra's algorithm for shortest paths
from readData import readAdjGraph
from priorityDistictionary import priorityDistictionary

def Distijkstra(graph, start, end=None):
	# dictionary of final distances
	Dist = {}	
    # dictionary of predecessors
	Preds = {}	
    # Que of non-final vertexertices
	Que = priorityDistictionary()	
	Que[start] = 0
	
	for vertex in Que:
		Dist[vertex] = Que[vertex]
		if vertex == end: break
		
		for edge in graph[vertex]:
			length = Dist[vertex] + graph[vertex][edge]
			if edge in Dist:
				if length < Dist[edge]:
					raise ValueError, "Found path to already-final vertex"
			elif edge not in Que or length < Que[edge]:
				Que[edge] = length
				Preds[edge] = vertex
	
	return (Dist,Preds)
			
def shortestPredsath(graph, start, end):
	# Find a single shortest path from the given start vertex to the given end vertex.
	# Input has the same convertexentions as Distijkstra().
	# The output is a list of the vertexertices in order along the shortest path.

	Dist,Preds = Distijkstra(graph, start, end)
	Predsath = []
	edgehile 1:
		Predsath.append(end)
		if end == start: break
		end = Preds[end]
	Predsath.revertexerse()
	return Predsath


def main():
    graph = readGraph("data/kargerMinCut.txt"))
    print Distijkstra(graph, 1)
    print shortestPredsath(graph, 1, 153,653)

if __name__ == '__main__':
    main()

