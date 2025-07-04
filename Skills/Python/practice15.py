#1
def bfs(graph, start):
    visited = []  # To store the visited nodes
    queue = [start]  # Initialize a queue with the starting node

    while queue:
        node = queue.pop(0)  # Dequeue a node from the queue
        if node not in visited:
            visited.append(node)  # Mark the node as visited
            # Enqueue all unvisited neighboring nodes
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
print("BFS traversal starting from node", start_node, ":", bfs(graph, start_node))


#2
def is_parenthesis_matched(equation):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in equation:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # If there are no opening brackets to match
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False  # If the closing bracket doesn't match the last opening bracket
    return len(stack) == 0  # True if all opening brackets are matched

# Example usage:
equation1 = "((a + b) * (c - d))"
equation2 = "((a + b) * (c - d)"
equation3 = "((a + b) * [c - d])"
equation4 = "{(a + b) * (c - d)}"
equation5 = "((a + b) * (c - d))"
print("Equation 1 parenthesis matched:", is_parenthesis_matched(equation1))
print("Equation 2 parenthesis matched:", is_parenthesis_matched(equation2))
print("Equation 3 parenthesis matched:", is_parenthesis_matched(equation3))
print("Equation 4 parenthesis matched:", is_parenthesis_matched(equation4))
print("Equation 5 parenthesis matched:", is_parenthesis_matched(equation5))


#3
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        return True


def kruskal(edges, num_vertices):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize an empty list to store the minimum spanning tree edges
    minimum_spanning_tree = []

    # Initialize disjoint set
    disjoint_set = DisjointSet(num_vertices)

    # Iterate through sorted edges and add edge to MST if it doesn't create a cycle
    for edge in edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.union(vertex1, vertex2):
            minimum_spanning_tree.append(edge)
            # Stop when number of edges in MST equals (num_vertices - 1)
            if len(minimum_spanning_tree) == num_vertices - 1:
                break

    return minimum_spanning_tree


# Example usage:
edges = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2),
         (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
         (6, 8, 6), (7, 8, 7)]
num_vertices = 9
minimum_spanning_tree = kruskal(edges, num_vertices)
print("Minimum Spanning Tree (Kruskal's algorithm):", minimum_spanning_tree)
