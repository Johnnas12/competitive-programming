'''
This Implementation is about graph representation in adjecence matrix
The graph is directed graph that means there is no mutual routes
'''

def create_graph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        
        mat[u][v] = 1
        
    return mat

if __name__ == "__main__":
    V = 3
    edges = [[0,1], [0, 2], [1, 2]]
    
    result_matrix = create_graph(V, edges)
    
    # The resultant matrix output
    for rows in result_matrix:
        print(rows)