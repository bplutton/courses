"""
Lab 16: Graphs — BFS and DFS

Graph class (complete — read and use it) and traversal functions (your job).
"""

from collections import deque


# ── Graph Class (provided) ─────────────────────────────────────────

class Graph:
    """An undirected graph using an adjacency list."""

    def __init__(self):
        self._adj = {}  # {label: [neighbor, ...]}

    def add_node(self, label):
        """Add a node to the graph. Does nothing if it already exists."""
        if label not in self._adj:
            self._adj[label] = []

    def add_edge(self, a, b):
        """Add an undirected edge between nodes a and b.

        Creates the nodes if they don't exist yet.
        """
        self.add_node(a)
        self.add_node(b)
        if b not in self._adj[a]:
            self._adj[a].append(b)
        if a not in self._adj[b]:
            self._adj[b].append(a)

    def get_neighbors(self, label):
        """Return the list of neighbors for the given node.

        Returns an empty list if the node doesn't exist.
        """
        return self._adj.get(label, [])

    def has_node(self, label):
        """Return True if the node exists in the graph."""
        return label in self._adj

    def nodes(self):
        """Return a list of all node labels."""
        return list(self._adj.keys())

    def __repr__(self):
        return f"Graph({dict(self._adj)})"


# ── Task 1: Build the Graph ───────────────────────────────────────

def build_lab_graph():
    """Build and return the lab graph.

    The graph looks like this:

        A
       / \\
      B   C
      |   |
      D   E
       \\ /
        F

    Edges: A-B, A-C, B-D, C-E, D-F, E-F
    """
    g = Graph()

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_node("E")
    g.add_node("F")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "F")
    g.add_edge("E", "F")

    return g


class DAGNode:
    def __init__(self, key):
        self.key = key
        self.children = set()
        self.parents = set()

    def __repr__(self):
        return f"DAGNode({self.key})"

    def add_child(self, node):
        if node is self:
            raise ValueError("No self-loops in a DAG node")
        self.children.add(node)
        node.parents.add(self)

    def add_dependency(self, node):
        """Declare that this node depends on `node` (node -> self)."""
        if node is self:
            raise ValueError("No self-dependency in a DAG node")

        # Prevent cycles: adding dependency node -> self would create a cycle if
        # node is already an ancestor of self (node depends on self transitively).
        if node.has_ancestor(self) or node is self:
            raise ValueError("Adding dependency would create a cycle")

        node.add_child(self)

    def has_ancestor(self, node):
        """Return True if `node` is a parent (direct or indirect) of this node."""
        if node is self:
            return False

        visited = set()
        stack = list(self.parents)

        while stack:
            cur = stack.pop()
            if cur is node:
                return True
            if cur not in visited:
                visited.add(cur)
                stack.extend(cur.parents)

        return False

    def remove_child(self, node):
        self.children.discard(node)
        node.parents.discard(self)

    @property
    def indegree(self):
        return len(self.parents)

    @property
    def outdegree(self):
        return len(self.children)

    def is_source(self):
        return self.indegree == 0

    def is_sink(self):
        return self.outdegree == 0


# ── Task 2: Breadth-First Search ──────────────────────────────────

def bfs(graph, start):
    """Traverse the graph in breadth-first order starting from `start`.

    Returns a list of node labels in the order they were visited.
    """
    visited = set()
    order = []
    frontier = deque()

    visited.add(start)
    frontier.append(start)

    while frontier:
        current = frontier.popleft()
        order.append(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append(neighbor)

    return order


# ── Task 3: Depth-First Search ────────────────────────────────────

def dfs(graph, start):
    """Traverse the graph in depth-first order starting from `start`.

    Returns a list of node labels in the order they were visited.
    Uses an iterative approach with a stack (not recursion).
    """
    visited = set()
    order = []
    stack = [start]

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        order.append(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                stack.append(neighbor)

    return order


# ── Task 4: Find Path ────────────────────────────────────────────

def find_path(graph, start, goal):
    """Find the shortest path from `start` to `goal` using BFS.

    Returns a list of node labels representing the path (including both
    start and goal). Returns an empty list if no path exists.
    """
    if start == goal:
        return [start]

    visited = set()
    frontier = deque()
    parent = {}

    visited.add(start)
    frontier.append(start)

    while frontier:
        current = frontier.popleft()

        if current == goal:
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                frontier.append(neighbor)

    return []  # No path found