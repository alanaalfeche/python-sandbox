"""
Adjancy list with list and dictionary

[V0] -> {V1: 0, V2: 0}
[V1] -> {V0: 2, V3: 0}
 .
 .
 . 

https://runestone.academy/runestone/books/published/pythonds/Graphs/Implementation.html
"""
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def add_neighbor(self, vertex, weight=0):
        self.connections[vertex] = weight
    
    def get_connections(self):
        return self.connections.keys()

    def get_id(self):
        return self.id

    def get_weight(self, vertex):
        return self.connections[vertex]

class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num = 0

    def get_vertex(self, n):
        if n in self.vertex_list:
            return self.vertex_list[n]
        else:
            return None
    
    def get_vertices(self):
        return self.vertex_list.keys()

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertex_list[key] = vertex
        self.num += 1
    
    def add_edge(self, fvertex, tvertex, weight=0):
        if fvertex not in self.vertex_list and tvertex not in self.vertex_list:
            return None
        self.vertex_list[fvertex].add_neighbor(self.vertex_list[tvertex], weight)

    def __contains__(self, n):
        return n in self.vertex_list

    def __iter__(self):
        return iter(self.vertex_list.values())

g = Graph()
for i in range(6):
    g.add_vertex(i)

g.add_edge(0, 1, 5)
