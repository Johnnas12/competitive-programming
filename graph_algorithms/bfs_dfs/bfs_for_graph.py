'''
This is breadth first search implementation of graph that utilize queue
Its really simple but tricky as we have to track the visited nodes otherwise it will stuck in some loop
'''
from collections import deque

def bfs(adj):
    source_node = 0  # here we can choose any source node
    seen = [source_node]  # this is list we will track of our seen or neighbour nodes
    
    q = deque() # initialize or queue here
    q.append(source_node)
    
    while q: # while elements from queue is finished being popped out
        node = q.popleft()
        
        for nei_node in adj[node]: # we will visit the neighbours of the current node
            if nei_node not in seen: # we first makes sure the node is not visited
                seen.append(nei_node) # add to seen list
                q.append(nei_node) # add it to queue from the right
    return seen


if __name__ == "__main__":
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(bfs(adj))