# All-Pairs Shortest Path:
## Brute Force (Repeated Dijkstra) vs. Floyd-Warshall (Dynamic Programming)

## Overview

This project compares two different algorithms for solving the **All-Pairs Shortest Path (APSP)** problem:

- **Repeated Dijkstra Algorithm (Brute Force / Greedy Approach)**
- **Floyd-Warshall Algorithm (Dynamic Programming)**

Both algorithms compute the shortest path between every pair of vertices in a weighted directed graph. The objective of this project is to compare their execution time on graphs of different sizes and densities, verify that they produce identical results, and analyze the trade-offs between the two approaches.

---

# Project Structure

```
Team3-Algo-Project/
│
├── algorithms.py
├── graph_input.py
├── main.py
├── Team3_All_Pairs_Shortest_Path_Paper.pdf
├── README.md

```

---

# Files Description

## algorithms.py

Contains the core implementation of:

- Repeated Dijkstra Algorithm
- Floyd-Warshall Algorithm
- Random Graph Generator

---

## graph_input.py

Responsible for:

- Reading a graph entered manually by the user.
- Building the adjacency list and adjacency matrix.
- Running both algorithms on the user-defined graph.
- Printing both shortest-path matrices.
- Verifying that both algorithms produce identical results.

---

## main.py

Responsible for:

- Displaying the interactive menu.
- Running benchmark experiments.
- Generating random graphs.
- Measuring execution time.
- Verifying correctness.
- Displaying a sample random graph.
- Drawing performance comparison figures.


```

The following modules are included with Python:

- time
- random
- math
- heapq

---

# How to Run

Run the project using:

```bash
python main.py
```

The program displays the following menu:

```
=========================================
All-Pairs Shortest Path Algorithm Comparison
=========================================

1. Run Benchmark Experiments
2. Enter Graph Manually
3. Display Sample Graph
4. Exit
```

---

# Program Features

### 1. Benchmark Experiments

Runs benchmark experiments on randomly generated graphs of different sizes and densities.

The program:

- Generates random graphs.
- Executes Repeated Dijkstra.
- Executes Floyd-Warshall.
- Verifies correctness.
- Measures execution times.
- Displays performance comparison graphs.

---

### 2. Manual Graph Input

Allows the user to enter a custom weighted directed graph.

Example:

```
Enter number of vertices: 5
Enter number of edges: 6

Enter each edge in the format:
source destination weight

Example:
0 1 5

Enter edge:
0 1 4
0 2 7
1 3 2
...
```

The program then prints:

- Repeated Dijkstra Result
- Floyd-Warshall Result
- Verification Passed!

---

### 3. Sample Graph Visualization

Displays a small randomly generated graph consisting of five vertices.

The visualization includes:

- Adjacency List
- Graph drawing using NetworkX
- Edge weights
- Node labels

This graph is generated only for demonstration purposes and is **not** used during benchmarking.

---

# Experimental Setup

The benchmark experiments use six graph configurations:

| Graph Size | Density |
|------------|----------|
| 50 Vertices | Sparse (10%) |
| 50 Vertices | Dense (90%) |
| 200 Vertices | Sparse (10%) |
| 200 Vertices | Dense (90%) |
| 400 Vertices | Sparse (10%) |
| 400 Vertices | Dense (90%) |

Each benchmark is executed **five times** using fixed random seeds to ensure reproducibility.

The reported execution time is the average of the five runs.

---

# Algorithms Compared

## Repeated Dijkstra

- Strategy: Greedy (Brute Force)
- Graph Representation: Adjacency List
- Data Structure: Priority Queue (Min-Heap)

### Time Complexity

```
O(V × E log V)
```

---

## Floyd-Warshall

- Strategy: Dynamic Programming
- Graph Representation: Adjacency Matrix

### Time Complexity

```
O(V³)
```

---

# Verification

The project verifies that **Repeated Dijkstra** and **Floyd-Warshall** produce identical shortest-path matrices for:

- Randomly generated benchmark graphs.
- Manually entered graphs.

If any mismatch is detected, the program raises an **AssertionError** or displays a verification failure message.

---

# Output

The project produces:

- Benchmark execution table.
- Verification messages.
- Execution Time Comparison graph.
- Graph Density Comparison graph.
- Sample Random Graph visualization.

---

# Authors

**Team 3**

- Zeyad Mohamed Samir (Team Leader)
- Norhan Hazem
- Habiba Essam
- Habiba Ahmed Hisham
- Myriam Hamam Ebrahim

Department of Computer Science

Misr International University (MIU)

---

# References

1. Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. *Introduction to Algorithms*, 3rd Edition.

2. Robert Sedgewick and Kevin Wayne. *Algorithms*, 4th Edition.

3. E. W. Dijkstra. *A Note on Two Problems in Connexion with Graphs*, 1959.

4. Robert W. Floyd. *Algorithm 97: Shortest Path*, 1962.

5. Stephen Warshall. *A Theorem on Boolean Matrices*, 1962.

6. NetworkX Documentation  
https://networkx.org/

7. Matplotlib Documentation  
https://matplotlib.org/
