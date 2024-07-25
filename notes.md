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

#### Algorithm for Topological Sort

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

## Trie Data Structure in Python

A Trie (pronounced as "try") is a type of search tree used to store a dynamic set or associative array where the keys are usually strings. It is also known as a prefix tree, as it can be searched by prefixes. Here’s a step-by-step guide to implementing a Trie and some common Trie operations.

### Trie Node Class

First, we need a `TrieNode` class to represent each node in the Trie. Each node can have multiple children (one for each character of the alphabet) and a flag to indicate whether the node marks the end of a word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
```

### Trie Class

The `Trie` class will contain methods to insert words, search for words, and search for prefixes.

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### Common Trie Algorithms

1. **Insert a word into the Trie**

    ```python
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    ```

2. **Search for a word in the Trie**

    ```python
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    ```

3. **Check if any word in the Trie starts with a given prefix**

    ```python
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    ```

### Full Implementation

Here's the full implementation of the Trie data structure:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: False
print(trie.starts_with("app"))  # Output: True
trie.insert("app")
print(trie.search("app"))     # Output: True
```

### Summary

- **TrieNode Class**: Represents each node with a dictionary of children and a boolean flag `is_end_of_word`.
- **Trie Class**: Contains methods to insert words, search for words, and check for prefixes.
- **Insert Method**: Adds a word to the Trie.
- **Search Method**: Checks if a word exists in the Trie.
- **Starts With Method**: Checks if any word in the Trie starts with a given prefix.

This implementation provides a basic and efficient way to handle a Trie in Python, which can be expanded with more advanced features as needed.

## Data Structures in Python: Space and Time Complexities

### List

- **Initialization**: `list()`, `[]`

#### Time and Space Complexities
- **Access**: O(1)
- **Search**: O(n)
- **Insertion**: O(n)
- **Deletion**: O(n)
- **Space Complexity**: O(n)

### Dictionary

- **Initialization**: `dict()`, `{}`

#### Time and Space Complexities
- **Access**: O(1)
- **Search**: O(1)
- **Insertion**: O(1)
- **Deletion**: O(1)
- **Space Complexity**: O(n)

### Set

- **Initialization**: `set()`, `{}`

#### Time and Space Complexities
- **Access**: O(1)
- **Search**: O(1)
- **Insertion**: O(1)
- **Deletion**: O(1)
- **Space Complexity**: O(n)

### Tuple

- **Initialization**: `tuple()`, `()`

#### Time and Space Complexities
- **Access**: O(1)
- **Search**: O(n)
- **Insertion**: Immutable (not applicable)
- **Deletion**: Immutable (not applicable)
- **Space Complexity**: O(n)

### Deque (from collections module)

- **Initialization**: `collections.deque()`

#### Time and Space Complexities
- **Access**: O(1)
- **Search**: O(n)
- **Insertion**: O(1)
- **Deletion**: O(1)
- **Space Complexity**: O(n)

### Stack (Using list)

- **Initialization**: `[]`

#### Time and Space Complexities
- **Access**: O(n)
- **Search**: O(n)
- **Insertion**: O(1)
- **Deletion**: O(1)
- **Space Complexity**: O(n)

### Queue (Using deque from collections module)

- **Initialization**: `collections.deque()`

#### Time and Space Complexities
- **Access**: O(n)
- **Search**: O(n)
- **Insertion**: O(1)
- **Deletion**: O(1)
- **Space Complexity**: O(n)

### Binary Search Tree (BST)

- **Initialization**: Custom implementation

#### Time and Space Complexities
- **Access**: O(log n) on average, O(n) in the worst case (unbalanced tree)
- **Search**: O(log n) on average, O(n) in the worst case (unbalanced tree)
- **Insertion**: O(log n) on average, O(n) in the worst case (unbalanced tree)
- **Deletion**: O(log n) on average, O(n) in the worst case (unbalanced tree)
- **Space Complexity**: O(n)

### Heap (using heapq module)

- **Initialization**: `heapq`

#### Time and Space Complexities
- **Access Min/Max**: O(1)
- **Insertion**: O(log n)
- **Deletion**: O(log n)
- **Space Complexity**: O(n)

### Graph

- **Initialization**: Adjacency list using `defaultdict(list)`

#### Time and Space Complexities
- **Access**: O(1) for adjacency list
- **Search (BFS/DFS)**: O(V + E) where V is the number of vertices and E is the number of edges
- **Insertion (Edge)**: O(1)
- **Deletion (Edge)**: O(1)
- **Space Complexity**: O(V + E) for adjacency list

This cheatsheet provides a quick reference for the time and space complexities of common operations for different data structures in Python.


Deleting a node from a Binary Search Tree (BST) involves several steps, depending on the node's position and the number of children it has. Here's a step-by-step guide to implementing the deletion algorithm, followed by the code:

### Deletion Cases

1. **Node with No Children (Leaf Node)**: Simply remove the node from the tree.
2. **Node with One Child**: Remove the node and replace it with its child.
3. **Node with Two Children**: Find the in-order successor (the smallest node in the right subtree) or the in-order predecessor (the largest node in the left subtree) to replace the node, and then delete the in-order successor or predecessor.

### Implementation

Here's the Python implementation of the BST deletion algorithm:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def delete_node(root, key):
    if not root:
        return root

    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Node to be deleted found
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node with two children
        # Get the inorder successor (smallest in the right subtree)
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)

    return root

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

# Example usage:
# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Deleting a node with value 3
root = delete_node(root, 3)
```

### Explanation

1. **TreeNode Class**: Defines a node in the BST, with a `value`, `left` child, and `right` child.

2. **delete_node Function**:
   - It takes `root` (the root of the tree or subtree) and `key` (the value of the node to be deleted).
   - The function first searches for the node to delete:
     - If `key` is less than `root.value`, it recurses on the left subtree.
     - If `key` is greater than `root.value`, it recurses on the right subtree.
     - If `key` is equal to `root.value`, the node to delete is found.
   - Depending on the node's children, the function handles three cases:
     - **No children**: Returns `None`.
     - **One child**: Returns the non-null child.
     - **Two children**: Finds the in-order successor using the `find_min` function, replaces the node's value with the in-order successor's value, and then deletes the in-order successor.

3. **find_min Function**:
   - This helper function finds the minimum value node in a subtree, which is used to find the in-order successor.

This implementation handles all cases for deleting a node in a BST while maintaining the BST properties.

To validate a binary search tree (BST) using recursion, you need to ensure that for each node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value. Here's a Python implementation:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(node, left=float('-inf'), right=float('inf')):
    # An empty tree is a valid BST
    if node is None:
        return True

    # The current node's value must be between the allowed bounds
    if not (left < node.value < right):
        return False

    # Recursively validate the left and right subtrees
    return (is_valid_bst(node.left, left, node.value) and
            is_valid_bst(node.right, node.value, right))

# Example usage:
# Creating a valid BST
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_bst(root))  # Output: True

# Creating an invalid BST
root_invalid = TreeNode(5)
root_invalid.left = TreeNode(1)
root_invalid.right = TreeNode(4, TreeNode(3), TreeNode(6))

print(is_valid_bst(root_invalid))  # Output: False
```

### Explanation:

1. **TreeNode Class**: Defines a simple binary tree node with a value, a left child, and a right child.

2. **is_valid_bst Function**:
   - It takes a `node` and two boundary values (`left` and `right`) to represent the allowed range of values for the node's value.
   - It checks if the `node` is `None` (base case) and returns `True` because an empty tree is a valid BST.
   - It then checks if the current node's value is within the allowed range (`left < node.value < right`). If not, it returns `False`.
   - It recursively validates the left and right subtrees, updating the bounds: the left subtree's values must be less than the current node's value, and the right subtree's values must be greater than the current node's value.

This implementation efficiently checks the BST property for each node by ensuring that all nodes in the left subtree are less than the node's value and all nodes in the right subtree are greater than the node's value.
