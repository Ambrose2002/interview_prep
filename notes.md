### **EXTENDED NOTES ON COMMON DSA's IN PYTHON**

### **Lists**
- **Initialization**: `lst = [1, 2, 3]`
- **Usage**:
  ```python
  lst = [1, 2, 3]
  lst.append(4)  # Add an item to the end of the list
  lst.extend([5, 6])  # Extend the list by appending elements from the iterable
  lst.insert(2, 'inserted')  # Insert an item at a given position
  lst.remove(1)  # Remove the first item with the value 1
  item = lst.pop()  # Remove and return the last item
  item = lst.pop(0)  # Remove and return the item at index 0
  lst.clear()  # Remove all items from the list
  index = lst.index(2)  # Return the index of the first item with the value 2
  count = lst.count(3)  # Return the number of times 3 appears in the list
  lst.sort()  # Sort the list in place
  lst.reverse()  # Reverse the elements of the list in place
  length = len(lst)  # Return the number of items in the list
  ```

### **Tuples**
- **Initialization**: `tup = (1, 2, 3)`
- **Usage**:
  ```python
  tup = (1, 2, 3)
  index = tup.index(2)  # Return the index of the first item with the value 2
  count = tup.count(3)  # Return the number of times 3 appears in the tuple
  ```

### **Dictionaries**
- **Initialization**: `d = {'key1': 'value1', 'key2': 'value2'}`
- **Usage**:
  ```python
  d = {'key1': 'value1', 'key2': 'value2'}
  keys = d.keys()  # Return a view object of all keys
  values = d.values()  # Return a view object of all values
  items = d.items()  # Return a view object of all key-value pairs
  value = d.get('key1', 'default_value')  # Return the value for 'key1', else 'default_value'
  d['key3'] = 'value3'  # Add or update an item
  d.update({'key4': 'value4'})  # Update the dictionary with elements from another dictionary
  value = d.pop('key2', 'default_value')  # Remove the specified key and return the value
  key, value = d.popitem()  # Remove and return a (key, value) pair
  d.clear()  # Remove all items from the dictionary
  ```

### **Sets**
- **Initialization**: `s = {1, 2, 3}`
- **Usage**:
  ```python
  s = {1, 2, 3}
  s.add(4)  # Add an element to the set
  s.remove(2)  # Remove the specified element
  s.discard(2)  # Remove the specified element without raising an error if not present
  item = s.pop()  # Remove and return an arbitrary set element
  s.clear()  # Remove all elements from the set
  union_set = s.union({5, 6})  # Return a new set with elements from both sets
  intersection_set = s.intersection({3, 4, 5})  # Return a new set with elements common to both sets
  difference_set = s.difference({2, 4})  # Return a new set with elements in the set that are not in the others
  symmetric_difference_set = s.symmetric_difference({3, 4, 5})  # Return a new set with elements in either set but not both
  ```

### **Strings**
- **Initialization**: `s = "hello"`
- **Usage**:
  ```python
  s = "hello world"
  words = s.split()  # Split the string into a list of substrings
  stripped = s.strip()  # Remove leading and trailing whitespace
  csv_text = "apple,banana,cherry"
  fruits = csv_text.split(',')  # Split by a specific delimiter
  joined = ' '.join(['hello', 'world'])  # Join elements of a list into a single string
  replaced = s.replace("world", "Python")  # Replace occurrences of substring 'world' with 'Python'
  index = s.find('world')  # Return the lowest index in the string where substring 'world' is found
  uppercase = s.upper()  # Convert to uppercase
  lowercase = s.lower()  # Convert to lowercase
  titlecase = s.title()  # Convert the first character of each word to uppercase
  capitalized = s.capitalize()  # Convert the first character to uppercase
  starts = s.startswith('hello')  # Check if the string starts with 'hello'
  ends = s.endswith('world')  # Check if the string ends with 'world'
  ```

### **Deque (from `collections` module)**
- **Initialization**: `from collections import deque`  
  `dq = deque([1, 2, 3])`
- **Usage**:
  ```python
  from collections import deque
  dq = deque([1, 2, 3])
  dq.append(4)  # Add to the right end
  dq.appendleft(0)  # Add to the left end
  item = dq.pop()  # Remove and return an element from the right end
  item = dq.popleft()  # Remove and return an element from the left end
  dq.extend([5, 6])  # Extend the right end
  dq.extendleft([-2, -1])  # Extend the left end
  dq.clear()  # Remove all elements
  dq.rotate(1)  # Rotate the deque 1 step to the right
  dq.rotate(-1)  # Rotate the deque 1 step to the left
  length = len(dq)  # Get the size of the deque
  ```

### **Heap (from `heapq` module)**
- **Initialization**: `import heapq`  
  `heap = []`
- **Usage**:
  ```python
  import heapq
  heap = []
  heapq.heappush(heap, 3)  # Push the value 3 onto the heap
  heapq.heappush(heap, 1)  # Push the value 1 onto the heap
  heapq.heappush(heap, 2)  # Push the value 2 onto the heap
  smallest = heapq.heappop(heap)  # Pop and return the smallest item
  heapq.heapify([3, 2, 1])  # Transform list into a heap
  largest_three = heapq.nlargest(3, heap)  # Get 3 largest elements
  smallest_three = heapq.nsmallest(3, heap)  # Get 3 smallest elements
  ```

### **Queue (from `queue` module)**
- **Initialization**: `import queue`  
  `q = queue.Queue()`
- **Usage**:
  ```python
  import queue
  q = queue.Queue()
  q.put(1)  # Put item into the queue
  q.put(2)
  item = q.get()  # Remove and return an item from the queue
  size = q.qsize()  # Get the size of the queue
  is_empty = q.empty()  # Check if the queue is empty
  is_full = q.full()  # Check if the queue is full
  ```

### **Examples**

#### List Example
```python
lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]
```

#### Dictionary Example
```python
d = {'a': 1, 'b': 2}
d['c'] = 3
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

#### Set Example
```python
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}
```

#### String Example
```python
s = "hello world"
print(s.upper())  # Output: "HELLO WORLD"
```

#### Deque Example
```python
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)
print(dq)  # Output: deque([1, 2, 3, 4])
```

#### Heap Example
```python
import heapq
heap = [3, 1, 4]
heapq.heapify(heap)
print(heap)  # Output: [1, 3, 4]
heapq.heappush(heap, 2)
print(heap)  # Output: [1, 2, 4, 3]
print(heapq.heappop(heap))  # Output: 1
print(heap)  # Output: [2, 3, 4]
```

#### Queue Example
```python
import queue
q = queue.Queue()
q.put(1)
q.put(2)
print(q.get())

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

### **Topological Sort**
Topological sorting is an algorithm used to order the vertices of a directed acyclic graph (DAG) such that for every directed edge \( uv \), vertex \( u \) comes before vertex \( v \). This is useful in scenarios like scheduling tasks, resolving symbol dependencies in compilers, and more.

### Algorithm for Topological Sort

There are two common methods to perform a topological sort:
1. **Kahn’s Algorithm (BFS-based)**
2. **Depth-First Search (DFS)-based Algorithm**

Here, we'll implement the DFS-based algorithm.

#### DFS-based Algorithm for Topological Sort

The idea is to perform a DFS traversal of the graph. During the traversal, we keep track of the visited nodes, and as we finish exploring a node, we add it to the front of a list (or use a stack). This ensures that nodes with no outgoing edges are processed first.

**Steps**
1. Create a recursive DFS function that marks the current node as visited and recurses for all its adjacent nodes.
2. Once all adjacent nodes are processed, push the current node onto a stack.
3. Repeat the process for all nodes in the graph.
4. The contents of the stack give the topological ordering.

**Implementation in Python**

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Dictionary containing adjacency List
        self.V = vertices               # Number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True  # Mark the current node as visited
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        # Push current vertex to stack which stores result
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.V  # Mark all the vertices as not visited
        stack = []  # Stack to store the result

        # Call the recursive helper function to store Topological Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        
        return stack

# Usage
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

result = g.topological_sort()
print("Topological Sort of the given graph:")
print(result)  # Expected Output: [5, 4, 2, 3, 1, 0] or any other valid topological order
```

**Explanation**

1. **Graph Initialization**: We initialize a graph using a `defaultdict` to hold the adjacency list representation of the graph.
2. **Adding Edges**: The `add_edge` function adds directed edges to the graph.
3. **DFS Utility Function**: The `topological_sort_util` function performs the DFS traversal. It marks the current node as visited, recurses for all adjacent nodes, and then inserts the current node at the beginning of the stack.
4. **Topological Sort Function**: The `topological_sort` function initializes the visited list and the stack. It then iterates over all the vertices, calling the DFS utility function for each unvisited node.
5. **Output**: The stack, which now contains the topological ordering of the vertices, is returned and printed.

This implementation ensures that the vertices are processed in a manner that satisfies the dependencies represented by the directed edges.

### Summary
- **BFS**: Uses a queue to explore nodes level by level.
- **DFS**: Uses a stack (explicit or recursion) to explore as far as possible along each branch.
- **Dijkstra's Algorithm**: Uses a priority queue to find the shortest path in a weighted graph with non-negative weights.
