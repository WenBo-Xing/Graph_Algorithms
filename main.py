import tkinter as tk 
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from algorithms import dijkstra_steps, prim_steps
from animation import animate_dijkstra, animate_prim
import os
from matplotlib.animation import PillowWriter


# ==== Global Variables ====

SAVE_DIR = "/Users/xingwenbo/Desktop/Dijkatra&Prim/animation/"
DIJKSTRA_GIF = os.path.join(SAVE_DIR, "dijkstra.gif")
PRIM_GIF = os.path.join(SAVE_DIR, "prim.gif")

# ==== Helper Functions ====
def getFileName(base_name, extension, directory):
        
    i = 0
    # check if file exists
    while True:
        filename = os.path.join(directory, f"{base_name}{f'{i}' if i > 0 else ''}.{extension}")
        path = os.path.join(directory, filename)
        if not os.path.exists(path):
            return filename
        i += 1

class GraphApp:
    
    def __init__(self, root):
        # root window
        self.root = root
        self.root.title("Graph Algorithm Visualizer")

        self.graph_adj = {}
        self.G = nx.Graph()

        # ==== Top UI Frame ====
        top_frame = tk.Frame(root)
        top_frame.pack(pady=10)

        tk.Label(top_frame, text="Graph Input (format: u v w per line)").pack()
        self.text_input = tk.Text(top_frame, height=10, width=60)
        self.text_input.pack()

        tk.Label(top_frame, text="Start Node:").pack()
        self.start_node_entry = tk.Entry(top_frame)
        self.start_node_entry.pack()

        # ==== Fringe Option ====
        fringe_frame = tk.Frame(root)
        fringe_frame.pack(pady=5)
        self.fringe_type = tk.StringVar(value="heap")
        tk.Label(fringe_frame, text="Fringe Type:").pack(side=tk.LEFT)
        tk.Radiobutton(fringe_frame, text="Binary Heap", variable=self.fringe_type, value="heap").pack(side=tk.LEFT)
        tk.Radiobutton(fringe_frame, text="Linked List", variable=self.fringe_type, value="list").pack(side=tk.LEFT)

        # ==== Buttons ====
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Run Dijkstra", command=self.run_dijkstra).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Run Prim", command=self.run_prim).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Add Edge", command=self.add_edge_dialog).pack(side=tk.LEFT, padx=5)

    def parse_graph(self):
        # clear graph
        self.graph_adj.clear()
        self.G.clear()
        lines = self.text_input.get("1.0", tk.END).strip().split('\n')
        for line in lines:
            if not line.strip():
                continue
            parts = line.strip().split()
            if len(parts) != 3:
                raise ValueError(f"Invalid edge line: {line}")
            u, v, w = parts[0], parts[1], float(parts[2])
            self.graph_adj.setdefault(u, {})[v] = w
            self.graph_adj.setdefault(v, {})[u] = w
            self.G.add_edge(u, v, weight=w)
    
    # Dijkstra's Algorithm
    def run_dijkstra(self):
        try:
            self.parse_graph()
            start = self.start_node_entry.get().strip()
            if start not in self.graph_adj:
                raise ValueError("Start node not in graph")
            steps = dijkstra_steps(self.graph_adj, start)
            pos = nx.spring_layout(self.G, seed=42)
            anim = animate_dijkstra(self.G, steps, pos)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        try:
            os.makedirs(os.path.dirname(DIJKSTRA_GIF), exist_ok=True)
            writer = PillowWriter(fps=1)
            # get unique filename
            dijkstra_path  = getFileName("dijkstra", "gif", SAVE_DIR)
            anim.save(dijkstra_path, writer=writer)
            plt.close('all')
            messagebox.showinfo("Success", f"Dijkstra animation saved successfully at\n{dijkstra_path}")
            play_gif(dijkstra_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save Dijkstra animation:\n{e}")

    # Prim's Algorithm
    def run_prim(self):
        
        try:
            # parse graph
            self.parse_graph()
            start = self.start_node_entry.get().strip()
            if start not in self.graph_adj:
                raise ValueError("Start node not in graph")
            # get steps
            steps = prim_steps(self.graph_adj, start)
            pos = nx.spring_layout(self.G, seed=42)
            anim = animate_prim(self.G, steps, pos)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        try:
            os.makedirs(os.path.dirname(PRIM_GIF), exist_ok=True)
            writer = PillowWriter(fps=1)
            prim_path = getFileName("prim", "gif", SAVE_DIR)
            anim.save(prim_path, writer=writer)
            plt.close('all')
            messagebox.showinfo("Success", f"Prim animation saved successfully at\n{prim_path}")
            play_gif(prim_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save Prim animation:\n{e}")

    # add edge dialog
    def add_edge_dialog(self):
        win = tk.Toplevel(self.root)
        win.title("Add Edge")

        tk.Label(win, text="Node U:").grid(row=0, column=0)
        u_entry = tk.Entry(win)
        u_entry.grid(row=0, column=1)

        tk.Label(win, text="Node V:").grid(row=1, column=0)
        v_entry = tk.Entry(win)
        v_entry.grid(row=1, column=1)

        tk.Label(win, text="Weight:").grid(row=2, column=0)
        w_entry = tk.Entry(win)
        w_entry.grid(row=2, column=1)

        # add edge
        def add():
            try:
                u = u_entry.get().strip()
                v = v_entry.get().strip()
                w = float(w_entry.get().strip())
                self.text_input.insert(tk.END, f"\n{u} {v} {w}")
                win.destroy()
            except:
                messagebox.showerror("Error", "Invalid edge input")

        tk.Button(win, text="Add", command=add).grid(row=3, columnspan=2)


# play gif animation
def play_gif(gif_path):
    try:
        from PIL import Image, ImageTk
    except ImportError:
        messagebox.showerror("Missing Dependency", "Please install Pillow (pip install pillow)")
        return

    win = tk.Toplevel()
    win.title("Play Animation")

    try:
        gif = Image.open(gif_path)
        frames = []
        while True:
            frame = ImageTk.PhotoImage(gif.copy())
            frames.append(frame)
            gif.seek(len(frames))
    except EOFError:
        pass
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load gif:\n{e}")
        return

    if not frames:
        return

    # show gif
    label = tk.Label(win)
    label.pack()

    delay = gif.info.get('duration', 100)

    def update_frame(index=0):
        
        label.config(image=frames[index])
        label._image = frames[index]  # type: ignore[attr-defined]
        next_index = (index + 1) % len(frames)
        win.after(delay, update_frame, next_index)

    update_frame(0)


if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = GraphApp(root)
        root.mainloop()
    except Exception as e:
        print("Failed to start GUI:", e)
        print("Make sure you are running this in an environment that supports tkinter and GUI operations.")
