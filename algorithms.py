import math
import heapq


# Dijkstra's Algorithm
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

# Prim's Algorithm
def prim(graph, start=None):
    """
    Compute the Minimum Spanning Tree (MST) using Prim's algorithm.
    :param graph: Adjacency list representation, e.g. {node: {neighbor: weight, ...}, ...}
    :param start: Start node (optional)
    :return: parent, where parent[v] is the parent of v in the MST
    """
    # get start node
    if start is None:
        start = next(iter(graph))
    # initialize parent, key, mst_set
    parent = {node: None for node in graph}
    key = {node: math.inf for node in graph}
    key[start] = 0
    mst_set = set()
    for _ in range(len(graph)):
        # Select the node not in MST with the minimum key value
        u = None
        u_key = math.inf
        # iterate over the graph
        for node in graph:
            # if the node is not in the MST and the key value is less than the current u_key, update the u_key and u
            if node not in mst_set and key[node] < u_key:
                u_key = key[node]
                u = node
        if u is None:
            break  # The graph may be disconnected
        mst_set.add(u)
        # iterate over the neighbors of the selected node
        for v, w in graph[u].items():
            if v not in mst_set and w < key[v]:
                key[v] = w
                parent[v] = u
    return parent

# Dijkstra's Algorithm with Steps
def dijkstra_steps(graph, start):
    """
    Get the tree edges at each step of Dijkstra's algorithm.
    :param graph: Adjacency list
    :param start: Start node
    :return: steps, a list of tree edge lists at each step
    """
    # initialize dist, prev, visited, pq, tree_edges, steps
    dist = {node: math.inf for node in graph}
    dist[start] = 0
    # initialize prev, visited, pq, tree_edges, steps
    prev = {node: None for node in graph}
    visited = set()
    pq = [(0, start)]
    tree_edges = []  # Current tree edges
    steps = [list(tree_edges)]  # Initial empty tree
    # iterate over the graph
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        # add the edge to the tree_edges
        if prev[u] is not None:
            tree_edges.append((prev[u], u))
        steps.append(list(tree_edges))
        # iterate over the neighbors of the selected node
        for v, w in graph[u].items():
            new_dist = d + w
            # if the new distance is less than the current distance, update the distance and previous node
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
    # get start node
    if start is None:
        start = next(iter(graph))
    # initialize parent, key, mst_set, mst_edges, steps
    parent = {node: None for node in graph}
    key = {node: math.inf for node in graph}
    key[start] = 0
    mst_set = set()
    mst_edges = []
    steps = [list(mst_edges)]
    # iterate over the graph
    for _ in range(len(graph)):
        # select the node not in MST with the minimum key value
        u = None
        u_key = math.inf
        # iterate over the graph
        for node in graph:
            if node not in mst_set and key[node] < u_key:
                u_key = key[node]
                u = node
        # if no node is found, break
        if u is None:
            break
        mst_set.add(u)
        # add the edge to the mst_edges
        if parent[u] is not None:
            mst_edges.append((parent[u], u))
        steps.append(list(mst_edges))
        # iterate over the neighbors of the selected node
        for v, w in graph[u].items():
            if v not in mst_set and w < key[v]:
                key[v] = w
                parent[v] = u
    # return the steps
    return steps
                                    
                
            