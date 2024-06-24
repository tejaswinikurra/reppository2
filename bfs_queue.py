graph={0: [1,6,7], 1:[0,2,4,5], 2:[3], 3:[2], 4:[1], 5:[1], 6:[0], 7:[8,9], 8:[7], 9:[7]}
start=0
queue=[start]
visited=set()
print(f"\nIterative DFS Traversal starting from vertex {start}")
#print("iterative DFS traversal starting from vertex {}".format(start))
while queue:
    vertex=queue.pop(0)
    #vertex has the vertices that are not visited
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add (vertex)
        #push unvisited neighbours onto the stack
        queue.extend(neighbour for neighbour in graph.get(vertex, [])if neighbour not in visited)
        #graph.get(vertex, []) gives the adjacents of the current vertex