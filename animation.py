import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx

# Dijkstra's Algorithm with Steps
def animate_dijkstra(graph, steps, pos=None):
    # get the position of the nodes
    if pos is None:
        pos = nx.spring_layout(graph)
    # get the edges of the graph
    fig, ax = plt.subplots()
    base_edges = list(graph.edges())
    labels = nx.get_edge_attributes(graph, 'weight')

    # prevent empty animation
    if not steps:
        steps = [[]]  

    def update(frame):
        ax.clear()
        # draw nodes
        nx.draw_networkx_nodes(graph, pos, node_color='lightblue', ax=ax)
        nx.draw_networkx_labels(graph, pos, ax=ax)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=8, ax=ax)
        # draw edges
        current_edges = steps[frame] if frame < len(steps) else steps[-1]
        nx.draw_networkx_edges(graph, pos, edgelist=base_edges, edge_color='gray', width=1, ax=ax)
        # draw current edges
        nx.draw_networkx_edges(graph, pos, edgelist=current_edges, edge_color='red', width=2, ax=ax)
        ax.set_title(f"Dijkstra's Algorithm - Step {frame}")
        return []

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1000, blit=False)
    return ani

# Prim's Algorithm with Steps
def animate_prim(graph, steps, pos=None):
    # get the position of the nodes
    if pos is None:
        pos = nx.spring_layout(graph)
    fig, ax = plt.subplots()
    # get the edges of the graph
    base_edges = list(graph.edges())
    labels = nx.get_edge_attributes(graph, 'weight')

    # prevent empty animation
    if not steps:
        steps = [[]]  

    # update function
    def update(frame):
        # clear the axes
        ax.clear()
        # draw nodes
        nx.draw_networkx_nodes(graph, pos, node_color='lightblue', ax=ax)
        # draw labels
        nx.draw_networkx_labels(graph, pos, ax=ax)
        # draw edge labels
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=8, ax=ax)
        # draw edges
        current_edges = steps[frame] if frame < len(steps) else steps[-1]
        nx.draw_networkx_edges(graph, pos, edgelist=base_edges, edge_color='gray', width=1, ax=ax)
        # draw current edges
        nx.draw_networkx_edges(graph, pos, edgelist=current_edges, edge_color='red', width=2, ax=ax)
        ax.set_title(f"Prim's Algorithm - Step {frame}")
        return []
    
    # create the animation
    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1000, blit=False)
    # return the animation
    return ani
