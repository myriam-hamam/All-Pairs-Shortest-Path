import math      # Gives us access to math.inf (Infinity), representing a road that doesn't exist

# Reuse the existing algorithms directly, instead of duplicating them here
from algorithms import repeated_dijkstra, floyd_warshall


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

    # Tell the user exactly how each edge line should be formatted before they start typing
    print("Enter each edge in the following format:")
    print("source destination weight")
    print("Example: 0 1 5")

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
        print("\nVerification Passed!")
        print("Repeated Dijkstra and Floyd-Warshall produced identical shortest paths.")
    else:
        print("\nVerification Failed!")
