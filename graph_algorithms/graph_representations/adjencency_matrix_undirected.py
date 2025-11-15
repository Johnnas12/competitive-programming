
'''
Adjacency Matrix for Undirected Graph is way of representing a graph using a 2D array.
Its way of representing graph as a bolean matrix of size V x V where V is number of vertices in the graph.
'''

def create_graph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        
        mat[u][v] = 1
        
        # since the graph is undirected it goes both ways so
        mat[v][u] = 1
    return mat


if __name__ == "__main__":
    V = 3
    edges = [[0,1], [0, 2], [1, 2]]        
    
    mat = create_graph(V, edges)
    # Adjecency Matrix representations
    for rows in mat:
        print(rows)