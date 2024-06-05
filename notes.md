#GRAPHS
Graphs are data structures that consist of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. Graphs can be directed or undirected. In a directed graph, edges have a direction (going from one vertex to another), whereas in an undirected graph, edges are bidirectional.

### **Graph Representation**
Graphs can be represented in multiple ways:
1. **Adjacency List**: Each vertex has a list of vertices it is connected to.
2. **Adjacency Matrix**: A 2D array where `matrix[i][j]` represents the presence of an edge between vertex `i` and vertex `j`.

### **Graph Traversal Algorithms**
Graph traversal algorithms explore all the vertices and edges in a graph.

#### **Breadth-First Search (BFS)**
BFS explores the graph level by level, starting from the source vertex and visiting all its neighbors before moving on to the neighbors' neighbors.

**Implementation**:
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
```

#### **Depth-First Search (DFS)**
DFS explores as far as possible along each branch before backtracking. It can be implemented using recursion or an explicit stack.

**Recursive Implementation**:
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')
```

**Iterative Implementation**:
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))  # Add neighbors in reverse order to visit in correct order

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs_iterative(graph, 'A')
```

### **Dijkstra's Algorithm**
Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative weights.

**Implementation**:
```python
import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, vertex) tuples
    pq = [(0, start)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If a shorter path to the current vertex has already been found, skip it
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example weighted graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 1},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 1, 'E': 1}
}

distances = dijkstra(graph, 'A')
print(distances)  # Output: {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 6, 'F': 5}
```

### Summary
- **BFS**: Uses a queue to explore nodes level by level.
- **DFS**: Uses a stack (explicit or recursion) to explore as far as possible along each branch.
- **Dijkstra's Algorithm**: Uses a priority queue to find the shortest path in a weighted graph with non-negative weights.
