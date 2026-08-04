import time      # Used to act as a stopwatch to measure how long algorithms take
import random    # Used to randomly generate the "roads" and "distances" for our fake maps
import matplotlib.pyplot as plt   # Used to draw the figures comparing the algorithms

from algorithms import repeated_dijkstra, floyd_warshall, generate_graphs

# Reuse the existing manual graph input feature, instead of duplicating it here
from graph_input import enter_graph_manually

# Fixed seed so every run of the experiments is reproducible, as described in the paper
RANDOM_SEED = 42

# Number of times each benchmark is repeated so we can compute an average execution time
NUM_TRIALS = 5


# ==========================================
# MAIN LAUNCHER (Interactive Menu)
# ==========================================

def display_menu():
    # Show the four available options to the user
    print("====================================")
    print("All-Pairs Shortest Path Algorithms")
    print("====================================")
    print("1. Run Benchmark Experiments")
    print("2. Enter Graph Manually")
    print("3. Display Sample Graph")
    print("4. Exit")


def main_menu():
    # Keep showing the menu until the user chooses to exit
    while True:
        display_menu()

        # A blank line before the prompt keeps the menu easy to read
        print()
        choice = input("Choose an option: ")

        # A separator line so the option's output is visually set apart from the menu
        print("----------------------------------------")

        if choice == "1":
            # Simply call the existing benchmark runner, unchanged
            run_benchmarks()
            print("\nPress Enter to return to the main menu...")
            input()

        elif choice == "2":
            # Let the user manually build and test a graph of their own
            enter_graph_manually()
            print("\nPress Enter to return to the main menu...")
            input()

        elif choice == "3":
            # Reuse the existing sample graph visualization, unchanged
            show_sample_graph_visualization()
            print("\nPress Enter to return to the main menu...")
            input()

        elif choice == "4":
            # Exit the program gracefully
            print("Thank you for using the All-Pairs Shortest Path Algorithms project.")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


# ==========================================
# 3. THE BENCHMARK SUITE (The Race Track)
# ==========================================

def run_benchmarks():
    # Before touching the real benchmarks, generate and display one small, easy-to-read
    # sample graph purely for visualization purposes (this graph is never benchmarked)
    show_sample_graph_visualization()

    # A list of the different races we want to run. 
    # Format: (Number of Cities, Map Density percentage, Label for the table)
    test_cases = [
        (50, 0.1, "Small Sparse (10% edges)"),
        (50, 0.9, "Small Dense (90% edges)"),
        (200, 0.1, "Medium Sparse (10% edges)"),
        (200, 0.9, "Medium Dense (90% edges)"),
        (400, 0.1, "Large Sparse (10% edges)"),
        (400, 0.9, "Large Dense (90% edges)")
    ]

    # Print the table headers. (The :<25 just tells Python to add spaces so columns line up nicely)
    print(f"{'Graph Type':<25} | {'Vertices':<8} | {'Dijkstra Time (s)':<18} | {'Floyd-Warshall Time (s)':<20}")
    print("-" * 80)

    # This will collect one summary record per test case, so we can plot everything afterwards
    results = []

    # Loop through our test cases one by one
    for V, density, name in test_cases:

        # These lists collect the timing of every trial so we can average them afterwards
        dijkstra_times = []
        fw_times = []

        # Run the benchmark multiple times, each trial with its own fixed, reproducible graph
        for trial in range(NUM_TRIALS):

            # Reset the seed to a different but fixed value per trial, so each trial's graph
            # is unique across trials, yet still exactly reproducible run after run
            random.seed(RANDOM_SEED + trial)

            # 1. Ask the map maker to build the cities and roads for this specific trial
            adj_list, matrix = generate_graphs(V, density)

            # 2. Test Dijkstra: Start stopwatch -> Run Algorithm -> Stop stopwatch -> Calculate elapsed time
            start_time = time.perf_counter()
            dijkstra_result = repeated_dijkstra(V, adj_list)
            dijkstra_time = time.perf_counter() - start_time
            dijkstra_times.append(dijkstra_time)

            # 3. Test Floyd-Warshall: Start stopwatch -> Run Algorithm -> Stop stopwatch -> Calculate elapsed time
            start_time = time.perf_counter()
            fw_result = floyd_warshall(V, matrix)
            fw_time = time.perf_counter() - start_time
            fw_times.append(fw_time)

            # Verify correctness: Repeated Dijkstra and Floyd-Warshall must agree on this trial's graph
            if dijkstra_result != fw_result:
                raise AssertionError(
                    f"Mismatch between Repeated Dijkstra and Floyd-Warshall results for test case '{name}' (trial {trial})!"
                )

        # All trials for this test case matched, so confirm it once for this benchmark
        print("Verification Passed: Repeated Dijkstra and Floyd-Warshall produced identical results.")

        # Compute the average execution time across all trials for each algorithm
        avg_dijkstra_time = sum(dijkstra_times) / NUM_TRIALS
        avg_fw_time = sum(fw_times) / NUM_TRIALS

        # 4. Print the final times for this round into our formatted table!
        print(f"{name:<25} | {V:<8} | {avg_dijkstra_time:<18.5f} | {avg_fw_time:<20.5f}")

        # Save this test case's summary so we can plot it later
        results.append({
            "name": name,
            "V": V,
            "density": density,
            "dijkstra_time": avg_dijkstra_time,
            "fw_time": avg_fw_time
        })

    # Once every benchmark has run and been verified, draw the comparison figures
    plot_execution_time_comparison(results)
    plot_effect_of_graph_density(results)


# ==========================================
# 5. GRAPH VISUALIZATION (The Map Preview)
# ==========================================

def show_sample_graph_visualization():
    # A separate, tiny, dedicated seed just for building the small sample graph, so it
    # never interferes with the fixed seeds used later by the real benchmark trials
    random.seed(RANDOM_SEED)

    # Build a small 5-city, 50% density graph, used ONLY for visualization, never benchmarked
    sample_adj_list, sample_matrix = generate_graphs(5, 0.5)

    # Show the small sample graph as text, then as a NetworkX drawing
    print_adjacency_list(sample_adj_list)
    visualize_graph(sample_adj_list)


def print_adjacency_list(adj_list):
    # A simple text preview of the small sample graph, so we can sanity-check it
    print("\nGenerated Sample Graph")

    # Go through every city in the order it was created
    for node in sorted(adj_list.keys()):
        # Build up a string of all "(neighbor,weight)" pairs for this city
        edges_text = " ".join(f"({neighbor},{weight})" for neighbor, weight in adj_list[node])
        print(f"{node} -> {edges_text}")

    # Blank line so the console output stays easy to read
    print()


def visualize_graph(adj_list):
    # Try to bring in NetworkX only when we actually need to draw a graph
    try:
        import networkx as nx
    except ImportError:
        # If NetworkX isn't installed, don't crash the whole benchmark, just skip drawing
        print("NetworkX is not installed. Skipping graph visualization.")
        return

    # Build a Directed Graph, since our roads only go one way (i -> j)
    graph = nx.DiGraph()

    # Add every city and every road (with its weight) into the NetworkX graph
    for node, edges in adj_list.items():
        # Make sure every city shows up as a node, even ones with no outgoing roads
        graph.add_node(node)
        for neighbor, weight in edges:
            graph.add_edge(node, neighbor, weight=weight)

    # Use a fixed seed so the layout (where nodes are placed) is reproducible every run
    layout = nx.spring_layout(graph, seed=42)

    plt.figure(figsize=(10, 8))

    # Draw the nodes and edges, with node labels shown
    nx.draw(graph, layout, with_labels=True, node_color="lightblue", node_size=600, arrows=True)

    # Pull out the weight of every edge so we can label them on the drawing
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, layout, edge_labels=edge_labels)

    plt.title("Generated Sample Graph (5 Vertices)")
    plt.tight_layout()

    plt.savefig("generated_random_graph.png")
    plt.show()
    plt.close()


# ==========================================
# 4. PLOTTING (The Figures)
# ==========================================

def plot_execution_time_comparison(results):
    # Pull out the labels and timings for every test case, in the same order they were run
    labels = [r["name"] for r in results]
    dijkstra_times = [r["dijkstra_time"] for r in results]
    fw_times = [r["fw_time"] for r in results]

    # Position of the points on the x-axis
    x_positions = range(len(labels))

    plt.figure(figsize=(12, 6))

    # Draw both algorithms as line charts with markers, instead of bars
    plt.plot(x_positions, dijkstra_times, marker="o", label="Repeated Dijkstra")
    plt.plot(x_positions, fw_times, marker="o", label="Floyd-Warshall")

    plt.xticks(list(x_positions), labels, rotation=30, ha="right")
    plt.ylabel("Average Execution Time (s)")
    plt.title("Execution Time Comparison: Repeated Dijkstra vs Floyd-Warshall")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("execution_time_comparison.png")
    plt.show()
    plt.close()


def plot_effect_of_graph_density(results):
    # Group the results by number of vertices, separating sparse and dense runs
    vertex_sizes = sorted(set(r["V"] for r in results))

    sparse_dijkstra = []
    dense_dijkstra = []
    sparse_fw = []
    dense_fw = []

    for V in vertex_sizes:
        # Find the sparse and dense record for this vertex size
        sparse_record = next(r for r in results if r["V"] == V and r["density"] < 0.5)
        dense_record = next(r for r in results if r["V"] == V and r["density"] >= 0.5)

        sparse_dijkstra.append(sparse_record["dijkstra_time"])
        dense_dijkstra.append(dense_record["dijkstra_time"])
        sparse_fw.append(sparse_record["fw_time"])
        dense_fw.append(dense_record["fw_time"])

    plt.figure(figsize=(12, 6))

    plt.plot(vertex_sizes, sparse_dijkstra, marker="o", label="Repeated Dijkstra (Sparse)")
    plt.plot(vertex_sizes, dense_dijkstra, marker="o", label="Repeated Dijkstra (Dense)")
    plt.plot(vertex_sizes, sparse_fw, marker="s", label="Floyd-Warshall (Sparse)")
    plt.plot(vertex_sizes, dense_fw, marker="s", label="Floyd-Warshall (Dense)")

    plt.xlabel("Number of Vertices")
    plt.ylabel("Average Execution Time (s)")
    plt.title("Effect of Graph Density on Execution Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("effect_of_graph_density.png")
    plt.show()
    plt.close()


# This is the "Start Button" for Python. It tells Python to launch the menu when we execute this file.
if __name__ == "__main__":
    main_menu()
