import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx

def animate_dijkstra(graph, steps, pos=None):
    if pos is None:
        pos = nx.spring_layout(graph)
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
        current_edges = steps[frame] if frame < len(steps) else steps[-1]
        nx.draw_networkx_edges(graph, pos, edgelist=base_edges, edge_color='gray', width=1, ax=ax)
        nx.draw_networkx_edges(graph, pos, edgelist=current_edges, edge_color='red', width=2, ax=ax)
        ax.set_title(f"Dijkstra's Algorithm - Step {frame}")
        return []

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1000, blit=False)
    return ani

def animate_prim(graph, steps, pos=None):
    if pos is None:
        pos = nx.spring_layout(graph)
    fig, ax = plt.subplots()
    base_edges = list(graph.edges())
    labels = nx.get_edge_attributes(graph, 'weight')

    # prevent empty animation
    if not steps:
        steps = [[]]  

    # update function
    def update(frame):
        ax.clear()
        nx.draw_networkx_nodes(graph, pos, node_color='lightblue', ax=ax)
        nx.draw_networkx_labels(graph, pos, ax=ax)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=8, ax=ax)
        current_edges = steps[frame] if frame < len(steps) else steps[-1]
        nx.draw_networkx_edges(graph, pos, edgelist=base_edges, edge_color='gray', width=1, ax=ax)
        nx.draw_networkx_edges(graph, pos, edgelist=current_edges, edge_color='red', width=2, ax=ax)
        ax.set_title(f"Prim's Algorithm - Step {frame}")
        return []

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1000, blit=False)
    return ani
