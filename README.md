# Performance Comparison of Repeated Dijkstra and Floyd-Warshall for the All-Pairs Shortest Path Problem

## Overview

This project compares two different algorithms for solving the **All-Pairs Shortest Path (APSP)** problem:

* **Repeated Dijkstra's Algorithm** (Greedy Approach)
* **Floyd-Warshall Algorithm** (Dynamic Programming)

Both algorithms compute the shortest path between every pair of vertices in a weighted graph. The objective is to compare their execution time on graphs of different sizes and densities and analyze the trade-offs between them.

---

## Project Structure
Project/
│
├── algorithms.py
├── main.py
├── algo project's graphs.py
├── Research paper
└── README.md
---

## Files Description

### algorithms.py

Contains the core implementation of:

* Repeated Dijkstra Algorithm
* Floyd-Warshall Algorithm
* Random Graph Generator

---

### main.py

Responsible for:

* Generating random graphs
* Running benchmark experiments
* Measuring execution times
* Verifying correctness of both algorithms
* Producing performance graphs
* Printing benchmark results

---

### algo project's graphs.py

Responsible for handling and plotting the performance and density comparison figures.

---

## Requirements

Python 3.10 or later

Required libraries:

```bash
pip install matplotlib
The following modules are also used:

time

random

math

heapq

(All except matplotlib are included with Python.)

How to Run
Run the project using:
python main.py
The program will:

Generate random graphs.

Execute Repeated Dijkstra.

Execute Floyd-Warshall.

Verify that both algorithms produce identical shortest-path results.

Measure and compare execution times.

Display and save performance graphs.

Output
The program prints a benchmark table similar to:

Graph Type                | Vertices | Dijkstra Time (s) | Floyd-Warshall Time (s)
-----------------------------------------------------------------------------------
Small Sparse              | 50       | 0.00231           | 0.01084
Small Dense               | 50       | 0.00863           | 0.00791
...
Experimental Setup
Graphs were generated using:

Vertices:

50

200

400

Graph densities:

Sparse (10%)

Dense (90%)

Each benchmark configuration is executed multiple times using fixed random seeds to ensure reproducibility, and the average execution time is reported.

Algorithms Compared
Repeated Dijkstra
Strategy: Greedy

Data Structure: Priority Queue (Min-Heap)

Graph Representation: Adjacency List

Time Complexity:

O(V² log V + VE log V)
Floyd-Warshall
Strategy: Dynamic Programming

Graph Representation: Adjacency Matrix

Time Complexity:

O(V³)
Verification
For every benchmark, the project compares the shortest-path matrices produced by both algorithms.

If any difference is detected, the program raises an AssertionError.

Authors
Zeyad Mohamed Samir

Norhan Hazem

Habiba Essam

Habiba Ahmed Hisham

Myriam Hamam Ebrahim

Department of Computer Science

Misr International University (MIU)

References
Thomas H. Cormen et al., Introduction to Algorithms, 3rd Edition.

Robert Sedgewick and Kevin Wayne, Algorithms, 4th Edition.

E. W. Dijkstra, "A Note on Two Problems in Connexion with Graphs", 1959.

Robert W. Floyd, "Algorithm 97: Shortest Path", 1962.

Stephen Warshall, "A Theorem on Boolean Matrices", 1962.
