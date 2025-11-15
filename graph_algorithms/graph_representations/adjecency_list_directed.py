'''
This implementation focuses on representing graphs in the list form,
The algorithm it really simple we will just append the neigbor vertices of current vertex

DIRECTED GRAPH
'''

def create_graph(V, edges):
    our_list = [[] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        
        our_list[u].append(v)
        
    return our_list

if __name__ == "__main__":
    V = 3
    edges = [[1, 0], [1, 2], [2, 0]]
    result = create_graph(V, edges)
    for rows in result:
        print(rows)