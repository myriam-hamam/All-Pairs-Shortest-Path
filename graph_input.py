import math      # Gives us access to math.inf (Infinity), representing a road that doesn't exist

# Reuse the existing algorithms directly, instead of duplicating them here
from algorithms import repeated_dijkstra, floyd_warshall

# Reuse the existing benchmark runner and sample graph visualization from main.py
from main import run_benchmarks, show_sample_graph_visualization


# ==========================================
# MAIN LAUNCHER (Interactive Menu)
# ==========================================

def display_menu():
    # Show the four available options to the user
    print("====================================")
    print("Graph Algorithms Project")
    print("====================================")
    print("1. Run Benchmark Experiments")
    print("2. Enter Graph Manually")
    print("3. Display Sample Graph")
    print("4. Exit")


def enter_graph_manually():
    # Ask the user how big their graph is
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    # Build an empty Adjacency List, in exactly the same format generate_graphs() produces
    adj_list = {i: [] for i in range(V)}

    # Build an empty Adjacency Matrix, in exactly the same format generate_graphs() produces
    matrix = [[math.inf] * V for _ in range(V)]

    # The distance from any city to itself is exactly 0 (same convention as generate_graphs())
    for i in range(V):
        matrix[i][i] = 0

    # Read every edge the user wants to enter
    for _ in range(E):
        edge_line = input("Enter edge (source destination weight): ")
        source, destination, weight = edge_line.split()
        source = int(source)
        destination = int(destination)
        weight = int(weight)

        # Add this edge to the Adjacency List format
        adj_list[source].append((destination, weight))

        # Add this exact same edge to the Adjacency Matrix format
        matrix[source][destination] = weight

    # Run both algorithms on the exact same manually entered graph
    dijkstra_result = repeated_dijkstra(V, adj_list)
    fw_result = floyd_warshall(V, matrix)

    # Print the Repeated Dijkstra distance matrix
    print("\nRepeated Dijkstra Result:")
    for row in dijkstra_result:
        print(row)

    # Print the Floyd-Warshall distance matrix
    print("\nFloyd-Warshall Result:")
    for row in fw_result:
        print(row)

    # Compare both results and report whether they agree
    if dijkstra_result == fw_result:
        print("\nVerification Passed:")
        print("Repeated Dijkstra and Floyd-Warshall produced identical shortest paths.")
    else:
        print("\nVerification Failed!")


def main_menu():
    # Keep showing the menu until the user chooses to exit
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            # Simply call the existing benchmark runner from main.py, unchanged
            run_benchmarks()

        elif choice == "2":
            # Let the user manually build and test a graph of their own
            enter_graph_manually()

        elif choice == "3":
            # Reuse the existing sample graph visualization from main.py, unchanged
            show_sample_graph_visualization()

        elif choice == "4":
            # Exit the program gracefully
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


# This is the "Start Button" for Python. It tells Python to launch the menu when we execute this file.
if __name__ == "__main__":
    main_menu()
