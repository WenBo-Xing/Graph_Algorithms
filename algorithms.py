import math
import heapq

def dijkstra(graph, start):
    """
    Compute the shortest paths using Dijkstra's algorithm.
    :param graph: Adjacency list representation, e.g. {node: {neighbor: weight, ...}, ...}
    :param start: Start node
    :return: (dist, prev) where dist is the shortest distance to each node, prev is the predecessor in the shortest path tree
    """
    dist = {node: math.inf for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    visited = set()
    pq = [(0, start)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u].items():
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))
    return dist, prev

def prim(graph, start=None):
    """
    Compute the Minimum Spanning Tree (MST) using Prim's algorithm.
    :param graph: Adjacency list representation, e.g. {node: {neighbor: weight, ...}, ...}
    :param start: Start node (optional)
    :return: parent, where parent[v] is the parent of v in the MST
    """
    if start is None:
        start = next(iter(graph))
    parent = {node: None for node in graph}
    key = {node: math.inf for node in graph}
    key[start] = 0
    mst_set = set()
    for _ in range(len(graph)):
        # Select the node not in MST with the minimum key value
        u = None
        u_key = math.inf
        for node in graph:
            if node not in mst_set and key[node] < u_key:
                u_key = key[node]
                u = node
        if u is None:
            break  # The graph may be disconnected
        mst_set.add(u)
        for v, w in graph[u].items():
            if v not in mst_set and w < key[v]:
                key[v] = w
                parent[v] = u
    return parent

def dijkstra_steps(graph, start):
    """
    Get the tree edges at each step of Dijkstra's algorithm.
    :param graph: Adjacency list
    :param start: Start node
    :return: steps, a list of tree edge lists at each step
    """
    dist = {node: math.inf for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    visited = set()
    pq = [(0, start)]
    tree_edges = []  # Current tree edges
    steps = [list(tree_edges)]  # Initial empty tree
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if prev[u] is not None:
            tree_edges.append((prev[u], u))
        steps.append(list(tree_edges))
        for v, w in graph[u].items():
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))
    return steps

def prim_steps(graph, start=None):
    """
    Get the tree edges at each step of Prim's algorithm.
    :param graph: Adjacency list
    :param start: Start node (optional)
    :return: steps, a list of tree edge lists at each step
    """
    if start is None:
        start = next(iter(graph))
    parent = {node: None for node in graph}
    key = {node: math.inf for node in graph}
    key[start] = 0
    mst_set = set()
    mst_edges = []
    steps = [list(mst_edges)]
    for _ in range(len(graph)):
        u = None
        u_key = math.inf
        for node in graph:
            if node not in mst_set and key[node] < u_key:
                u_key = key[node]
                u = node
        if u is None:
            break
        mst_set.add(u)
        if parent[u] is not None:
            mst_edges.append((parent[u], u))
        steps.append(list(mst_edges))
        for v, w in graph[u].items():
            if v not in mst_set and w < key[v]:
                key[v] = w
                parent[v] = u
    return steps
                                    
                
            