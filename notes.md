### Notes on Trees and Common Algorithms

### **Trees**

A tree is a hierarchical data structure that consists of nodes, with a single node designated as the root. Each node may have zero or more child nodes. Trees are used to represent hierarchical relationships and are a fundamental data structure in computer science.

#### **Basic Terminology**
- **Node**: Basic unit of a tree containing a value or data and references to its children.
- **Root**: The top node of the tree.
- **Parent**: A node that has one or more children.
- **Child**: A node that descends from another node.
- **Leaf**: A node with no children.
- **Subtree**: A tree formed by a node and its descendants.
- **Depth**: The length of the path from the root to the node.
- **Height**: The length of the path from the node to the deepest leaf.

### **Binary Trees**
A binary tree is a tree in which each node has at most two children, referred to as the left child and the right child.

#### **Common Operations**
- **Insertion**
- **Deletion**
- **Traversal** (Inorder, Preorder, Postorder)
- **Searching**

#### **Tree Traversal Algorithms**
Traversal refers to the process of visiting all the nodes in a tree in a specific order.

1. **Inorder Traversal (Left, Root, Right)**
    - Visit the left subtree
    - Visit the root
    - Visit the right subtree
    ```python
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.val)
            inorder_traversal(root.right)
    ```

2. **Preorder Traversal (Root, Left, Right)**
    - Visit the root
    - Visit the left subtree
    - Visit the right subtree
    ```python
    def preorder_traversal(root):
        if root:
            print(root.val)
            preorder_traversal(root.left)
            preorder_traversal(root.right)
    ```

3. **Postorder Traversal (Left, Right, Root)**
    - Visit the left subtree
    - Visit the right subtree
    - Visit the root
    ```python
    def postorder_traversal(root):
        if root:
            postorder_traversal(root.left)
            postorder_traversal(root.right)
            print(root.val)
    ```

4. **Level Order Traversal (Breadth-First Search)**
    - Visit nodes level by level from left to right
    ```python
    from collections import deque

    def level_order_traversal(root):
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    ```

### **Binary Search Tree (BST)**
A binary search tree is a binary tree in which every node's left child contains a value less than its parent node, and every right child contains a value greater than its parent node.

#### **Common Operations**
- **Insertion**
    ```python
    def insert(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root
    ```

- **Search**
    ```python
    def search(root, val):
        if not root or root.val == val:
            return root
        if val < root.val:
            return search(root.left, val)
        return search(root.right, val)
    ```

- **Deletion**
    ```python
    def delete_node(root, key):
        if not root:
            return root
        if key < root.val:
            root.left = delete_node(root.left, key)
        elif key > root.val:
            root.right = delete_node(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = min_value_node(root.right)
            root.val = temp.val
            root.right = delete_node(root.right, temp.val)
        return root

    def min_value_node(node):
        current = node
        while current.left:
            current = current.left
        return current
    ```

### **Balanced Trees**
Balanced trees are special types of binary trees that maintain their height to be logarithmic with respect to the number of nodes, ensuring efficient operations.

#### **AVL Tree**
An AVL tree is a self-balancing binary search tree where the difference in heights of the left and right subtrees of any node is at most one.

#### **Red-Black Tree**
A red-black tree is a self-balancing binary search tree where nodes have an extra color attribute that ensures the tree remains approximately balanced during insertions and deletions.

### **Heaps**
A heap is a special tree-based data structure that satisfies the heap property. There are two types of heaps:

1. **Min-Heap**: The key at the root must be the minimum among all keys in the heap. The same property must be recursively true for all nodes.
2. **Max-Heap**: The key at the root must be the maximum among all keys in the heap. The same property must be recursively true for all nodes.

#### **Common Operations**
- **Insertion**: Insert the new key at the end of the tree and then heapify up.
- **Deletion**: Remove the root and replace it with the last element, then heapify down.
- **Heapify**: Ensure the tree satisfies the heap property.

#### **Implementation Using Python's `heapq` Module**
```python
import heapq

# Min-Heap
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
smallest = heapq.heappop(min_heap)

# Max-Heap (Using negation)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)
largest = -heapq.heappop(max_heap)
```
### **GRAPHS**
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
