# Implement Breadth First Search algorithm. 
# Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph
# or tree data structure.

# bfs 
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = [] #Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print (s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print(" Following is the path using breadth first search: ")
bfs(visited, graph, 'A')