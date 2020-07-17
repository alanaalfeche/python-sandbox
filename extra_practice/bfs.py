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


def bfs(graph, node):
    """
    BFS is a tree traveral algorithm that traverses the tree level by level. 
    Time complexity for BFS on a graph is O(V + E); where V is the number of vertices and E is the number of edges.
    """
    visited, queue = [], []
    visited.append(node)
    queue.append(node)
    result = ""

    while queue:
        s = queue.pop(0)
        result += s

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    
    return result

ans = bfs(graph, 'A')
print(ans)