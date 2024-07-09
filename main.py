
### 2. `main.py`

"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
"""




def longest_path(graph: list) -> int:
    # Your implementation goes here
    topo_sort = topological_sort(graph);
    return calculate_longest_path(graph, topo_sort);

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    from collections import deque

    n = len(graph);
    visited=[0]*n
    indeg=[0]*n
    res=[]
    q=deque()
    
    for i in range(n) :
        for j,w in graph[i]:
            indeg[j]+=1
    
    for i in range(n) :
        if indeg[i]==0:
            q.append(i);

    while q:
        u=q.popleft()
        res.append(u)
        for i,w in graph[u]:
            indeg[i]-=1
            if indeg[i]==0:
                q.append(i)
    
    return res

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    n = len(graph);
    dist = [-float('inf')] * n

    for i in range(len(topo_order)):
        if topo_order[i]==0:
            dist[i]=0

    for u in topo_order:
        if dist[u]!= -float('inf'):
            for v, wt in graph[u]:
                if dist[u] + wt > dist[v]:
                    dist[v] = wt + dist[u]
    
    return max(dist)
