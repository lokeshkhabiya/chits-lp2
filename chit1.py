# Implement depth first search algorithm. Use an undirected 
#graph and develop a recursive algorithm for searching all
# the vertices of a graph or tree data structure.

# DFS 
graph = {
    "A": ['B', 'C'],
    "B": ['D', 'E'],
    "C": ['F'],
    "D": [],
    "E": ['F'],
    "F": []
}

# visit to keep track of visited  nodes 
visit = set();

def dfs(visit, graph, node):
    if node not in visit: 
        print(node, end = " ")
        visit.add(node);
        for neighbour in graph[node]:
            dfs(visit, graph, neighbour)

# example 
print(" Following is the path using depth first search: ")
dfs(visit, graph, 'A')