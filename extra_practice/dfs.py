"""
            A
        B       C
    D       E       F     

"""

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = set()
result = ""
def dfs(visited, graph, node):
    """
    DFS is a tree traveral algorithm that traverses the tree going forward. Uses "backtracking" to go to the next node. 
    Time complexity for BFS on a graph is O(V + E); where V is the number of vertices and E is the number of edges.
    """
    global result
    if node not in visited:
        result += node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

dfs(visited, graph, 'A')
print(result)