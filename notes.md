Dijkstra's algorithm is a popular algorithm for finding the shortest paths from a single source vertex to all other vertices in a graph. The graph can be represented with non-negative weights. Here's a step-by-step explanation of the algorithm along with the implementation in Python.

### Steps of Dijkstra's Algorithm

1. **Initialization**:
    - Create a priority queue (min-heap) to store the vertices to be explored, prioritized by their current known shortest distance from the source.
    - Set the distance to the source vertex as 0 and all other vertices as infinity.
    - Track the shortest path tree using a dictionary that maps each vertex to its shortest distance from the source.

2. **Processing**:
    - While the priority queue is not empty:
        1. Extract the vertex with the smallest known distance from the priority queue.
        2. For each neighboring vertex of the extracted vertex, calculate the potential new path distance.
        3. If the calculated path distance is shorter than the known distance, update the shortest path distance and add the neighboring vertex to the priority queue with the updated distance.

3. **Completion**:
    - Once all vertices have been processed, the shortest path distances from the source to all vertices are known.

### Python Implementation

```python
import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, vertex) tuples
    priority_queue = [(0, start)]
    # Dictionary to track shortest known distances from start
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    while priority_queue:
        # Extract the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If a shorter path to current_vertex has already been found, skip processing
        if current_distance > distances[current_vertex]:
            continue

        # Explore each neighbor of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

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

# Running Dijkstra's algorithm from vertex 'A'
distances = dijkstra(graph, 'A')
print(distances)  # Output: {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 6, 'F': 5}
```

### Explanation of the Implementation

1. **Initialization**:
    - `priority_queue` is a list initialized with a tuple containing the starting vertex and a distance of 0.
    - `distances` is a dictionary where the keys are vertices and the values are the shortest known distances from the start vertex. All distances are initially set to infinity, except for the start vertex which is set to 0.

2. **Main Loop**:
    - The algorithm uses a while loop to process the priority queue until it is empty.
    - In each iteration, it extracts the vertex with the smallest distance (`current_distance, current_vertex = heapq.heappop(priority_queue)`).
    - If a shorter distance to `current_vertex` has already been found (`if current_distance > distances[current_vertex]`), it skips further processing of this vertex.
    - For each neighbor of the current vertex, it calculates the new distance (`distance = current_distance + weight`).
    - If this new distance is shorter than the known distance, it updates the shortest distance and pushes the neighbor onto the priority queue with the updated distance.

3. **Completion**:
    - After the priority queue is empty, the dictionary `distances` contains the shortest path distances from the start vertex to all other vertices.

### Key Points
- **Priority Queue**: Efficiently extracts the vertex with the smallest known distance.
- **Distance Updates**: Only updates distances if a shorter path is found.
- **Graph Representation**: Uses an adjacency list where each vertex maps to its neighbors and corresponding edge weights.

This implementation of Dijkstra's algorithm efficiently finds the shortest paths in a graph with non-negative weights.
