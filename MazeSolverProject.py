import tkinter as tk
import heapq
import time
import random

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_obstacle = False
        self.cost = float('inf')
        self.heuristic = 0
        self.parent = None

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

class PathfindingSolver:
    def __init__(self, root, rows, cols):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.grid = [[Node(row, col) for col in range(cols)] for row in range(rows)]
        self.start_node = None
        self.goal_node = None
        self.first_reset = True
        self.skip_flag = False
        self.algorithm = "Dijkstra"

        self.canvas = tk.Canvas(root, width=cols * 30, height=rows * 30, borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        self.visited_nodes_label = tk.Label(root, text="Visited Nodes: 0", font=("Helvetica", 12))
        self.visited_nodes_label.grid(row=1, column=0, pady=10)

        self.path_nodes_label = tk.Label(root, text="Path Nodes: 0", font=("Helvetica", 12))
        self.path_nodes_label.grid(row=2, column=0, pady=10)

        self.algorithm_label = tk.Label(root, text=f"Algorithm: {self.algorithm}", font=("Helvetica", 12))
        self.algorithm_label.grid(row=3, column=0, pady=10)

        self.solve_button = tk.Button(root, text="Solve Maze", command=self.solve_maze)
        self.solve_button.grid(row=4, column=0, pady=10)

        self.skip_button = tk.Button(root, text="Skip", command=self.skip_steps)
        self.skip_button.grid(row=5, column=0, pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_maze)
        self.reset_button.grid(row=6, column=0, pady=10)

        self.algorithm_button = tk.Button(root, text="Switch Algorithm", command=self.switch_algorithm)
        self.algorithm_button.grid(row=7, column=0, pady=10)

        self.canvas.bind("<B1-Motion>", self.toggle_obstacle)
        self.canvas.bind("<Button-1>", self.toggle_start_goal)

        self.generate_random_maze()

    def init_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1 = col * 30, row * 30
                x2, y2 = x1 + 30, y1 + 30
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="grid")

    def generate_random_maze(self):
        self.init_grid()
        start_row, start_col = random.randint(1, self.rows - 2), random.randint(1, self.cols - 2)
        end_row, end_col = random.randint(1, self.rows - 2), random.randint(1, self.cols - 2)
        self.start_node = self.grid[start_row][start_col]
        self.goal_node = self.grid[end_row][end_col]

        for row in range(2, self.rows - 2):
            for col in range(2, self.cols - 2):
                if random.random() < 0.2:
                    self.grid[row][col].is_obstacle = True

        self.draw_maze()

    def reset_maze(self):
        self.canvas.delete("all")
        self.start_node = None
        self.goal_node = None

        for row in range(self.rows):
            for col in range(self.cols):
                node = self.grid[row][col]
                if node.is_obstacle:
                    node.is_obstacle = False
                    x1, y1 = col * 30, row * 30
                    x2, y2 = x1 + 30, y1 + 30
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="grid")

        if not self.first_reset:
            self.first_reset = True
            self.generate_random_maze()
        else:
            self.init_grid()

        self.visited_nodes_label.config(text="Visited Nodes: 0")
        self.path_nodes_label.config(text="Path Nodes: 0")

    def skip_steps(self):
        self.skip_flag = True

    def draw_maze(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1 = col * 30, row * 30
                x2, y2 = x1 + 30, y1 + 30

                if self.grid[row][col] == self.start_node:
                    color = "green"
                    # self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="grid")
                elif self.grid[row][col] == self.goal_node:
                    color = "red"
                    # self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="grid")
                elif self.grid[row][col].is_obstacle:
                    color = "black"
                    # self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="grid")
                else:
                    color = "white"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="grid")

    def toggle_obstacle(self, event):
        col = int(event.x / 30)
        row = int(event.y / 30)
        if 0 <= row < self.rows and 0 <= col < self.cols:
            node = self.grid[row][col]
            node.is_obstacle = not node.is_obstacle
            color = "black" if node.is_obstacle else "white"
            self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill=color, tags="grid")

    def toggle_start_goal(self, event):
        col = int(event.x / 30)
        row = int(event.y / 30)
        if 0 <= row < self.rows and 0 <= col < self.cols:
            clicked_node = self.grid[row][col]

            if self.start_node is None:
                self.start_node = clicked_node
                self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="green", tags="grid")
            elif self.goal_node is None and clicked_node != self.start_node:
                self.goal_node = clicked_node
                self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="red", tags="grid")
            elif clicked_node == self.start_node:
                self.start_node = None
                self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="white", tags="grid")
            elif clicked_node == self.goal_node:
                self.goal_node = None
                self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="white", tags="grid")

    def switch_algorithm(self):
        if self.algorithm == "Dijkstra":
            self.algorithm = "A*"
            self.algorithm_label.config(text="Algorithm: A*")
        else:
            self.algorithm = "Dijkstra"
            self.algorithm_label.config(text="Algorithm: Dijkstra")

    def solve_maze(self):
        open_set = [self.start_node]
        self.start_node.cost = 0
        visited_nodes = set()

        while open_set:
            current_node = heapq.heappop(open_set)
            if current_node == self.goal_node:
                self.draw_path()
                break

            visited_nodes.add(current_node)
            for neighbor in self.get_neighbors(current_node):
                tentative_cost = current_node.cost + 1
                if tentative_cost < neighbor.cost and not neighbor.is_obstacle:
                    neighbor.cost = tentative_cost
                    neighbor.parent = current_node

                    if self.algorithm == "A*":
                        neighbor.heuristic = abs(neighbor.row - self.goal_node.row) + abs(neighbor.col - self.goal_node.col)

                    heapq.heappush(open_set, neighbor)
                    self.display_step(neighbor)
                    if not self.skip_flag:
                        time.sleep(0.1)
                    self.root.update()

                    self.visited_nodes_label.config(text=f"Visited Nodes: {len(visited_nodes)}")

    def get_neighbors(self, node):
        neighbors = []
        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for row_offset, col_offset in offsets:
            row, col = node.row + row_offset, node.col + col_offset
            if 0 <= row < self.rows and 0 <= col < self.cols:
                neighbors.append(self.grid[row][col])
        return neighbors

    def draw_path(self):
        current_node = self.goal_node
        path_nodes = 0
        while current_node:
            row, col = current_node.row, current_node.col
            if current_node != self.start_node and current_node != self.goal_node:
                self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="blue", tags="grid")
                path_nodes += 1

            current_node = current_node.parent

        self.path_nodes_label.config(text=f"Path Nodes: {path_nodes + 2}")

    def display_step(self, node):
        if node != self.goal_node and node != self.start_node:
            row, col = node.row, node.col
            self.canvas.create_rectangle(col * 30, row * 30, (col + 1) * 30, (row + 1) * 30, fill="yellow", tags="grid")
            if not self.skip_flag:
                time.sleep(0.1)
            self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pathfinding Algorithm Visualization")
    app = PathfindingSolver(root, rows=20, cols=20)
    root.mainloop()