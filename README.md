# Maze-Solver

A Python-based pathfinding algorithm visualization tool that demonstrates Dijkstra's algorithm and A* search in an interactive maze environment.

## Features

- **Interactive Maze Creation**: Click and drag to create obstacles, or use the random maze generator
- **Dual Algorithm Support**: Switch between Dijkstra's algorithm and A* search
- **Visual Pathfinding**: Watch algorithms explore the maze in real-time with color-coded visualization
- **Performance Metrics**: Track visited nodes and path length
- **User Controls**: Start/goal placement, skip animation, and maze reset functionality

## Visual Guide

- 🟢 **Green**: Start node
- 🔴 **Red**: Goal node
- ⚫ **Black**: Obstacles/walls
- 🟡 **Yellow**: Nodes being explored
- 🔵 **Blue**: Final optimal path
- ⚪ **White**: Open spaces

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Mazza-Solver.git
cd Mazza-Solver
```

2. Ensure you have Python 3.x installed with tkinter support:
```bash
python --version
```

3. Run the application:
```bash
python MazzaSolverProject.py
```

## Usage

### Basic Controls
- **Left Click**: Place start node (first click) or goal node (second click)
- **Click and Drag**: Create or remove obstacles
- **Solve Maze**: Start pathfinding algorithm
- **Skip**: Speed up visualization by skipping animation delays
- **Reset**: Clear the maze and start over
- **Switch Algorithm**: Toggle between Dijkstra and A*

### Creating a Maze
1. Run the program - it will generate a random maze automatically
2. Or click "Reset" to start with a blank grid
3. Click once to place the start node (green)
4. Click again to place the goal node (red)
5. Drag to create obstacles (black squares)
6. Click "Solve Maze" to watch the algorithm find the path

### Algorithm Comparison
- **Dijkstra**: Guarantees shortest path but explores uniformly in all directions
- **A***: Uses heuristic (Manhattan distance) to guide search toward goal, often faster

## Technical Details

### Algorithms Implemented
- **Dijkstra's Algorithm**: Classic shortest-path algorithm using uniform cost search
- **A* Search**: Heuristic-based pathfinding using Manhattan distance

### Grid System
- 20x20 grid with 8-directional movement (including diagonals)
- Each cell is 30x30 pixels
- Supports dynamic obstacle placement

### Performance Metrics
- **Visited Nodes**: Number of nodes explored during search
- **Path Nodes**: Length of the final path found

## Code Structure

```
MazzaSolverProject.py
├── Node class          # Represents individual grid cells
├── PathfindingSolver   # Main application class
    ├── Grid management
    ├── UI components
    ├── Event handling
    └── Algorithm implementation
```

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- No external dependencies required

## Future Enhancements

- [ ] Additional algorithms (BFS, DFS, Greedy Best-First)
- [ ] Adjustable grid size
- [ ] Maze import/export functionality
- [ ] Performance benchmarking
- [ ] Different heuristic functions for A*

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-algorithm`)
3. Commit your changes (`git commit -am 'Add new pathfinding algorithm'`)
4. Push to the branch (`git push origin feature/new-algorithm`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Screenshots

The application features a clean, intuitive interface with real-time visualization of pathfinding algorithms in action. Watch as the algorithms explore the maze and find the optimal path from start to goal.

## Author

Mohamed Taha Khattab - mohamed.taha.khattab0@gmail.com

---

*Created as an educational tool for understanding pathfinding algorithms and their visualization.*
