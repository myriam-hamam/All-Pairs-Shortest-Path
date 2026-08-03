import math      # Gives us access to math.inf (Infinity), representing a road that doesn't exist
import random    # Used to randomly generate the "roads" and "distances" for our fake maps
import heapq     # A specialized sorting tool (Priority Queue) that Dijkstra uses to always find the closest city fast


# ==========================================
# 1. THE ALGORITHMS
# ==========================================
# dijkstra

def repeated_dijkstra(V, adj_list):
    # This list will hold our final "cheat sheet" of all shortest paths
    all_pairs_shortest_paths = []
    
    # Loop through every single city to use it as a starting point (This makes it "All-Pairs")
    for start_node in range(V):
        
        # Set the distance to all cities to Infinity (because we haven't explored them yet)
        distances = {node: math.inf for node in range(V)}
        
        # The distance from our starting city to itself is always 0
        distances[start_node] = 0
        
        # The Priority Queue (pq). We put our starting city in it. Format: (distance_from_start, city_node)
        pq = [(0, start_node)]
        
        # Keep exploring as long as there are cities in our queue
        while pq:
            # Pop out the city that is currently the closest to our starting point
            current_dist, current_node = heapq.heappop(pq)
            
            # Optimization: If we somehow pulled out an old, longer path from the queue, ignore it
            if current_dist > distances[current_node]:
                continue
            
            # Look at every neighboring city connected to the city we are currently standing in
            for neighbor, weight in adj_list[current_node]:
                # Calculate the total distance to this neighbor if we travel through the current city
                distance = current_dist + weight
                
                # If this new calculated distance is shorter than the best route we knew before...
                if distance < distances[neighbor]:
                    # Update our record book with this new, faster shortcut
                    distances[neighbor] = distance
                    # Put this neighbor into the queue so we can explore outwards from it later
                    heapq.heappush(pq, (distance, neighbor))
                    
        # After fully exploring the map from 'start_node', save its row of results to our final cheat sheet
        all_pairs_shortest_paths.append([distances[i] for i in range(V)])
        
    # Return the completed cheat sheet
    return all_pairs_shortest_paths
#floyd warshall

def floyd_warshall(V, adj_matrix):
    # Create a copy of the input map matrix so we don't destroy the original data. 
    # 'dp' stands for Dynamic Programming table.
    dp = [row[:] for row in adj_matrix]
    
    # The magic of Floyd-Warshall: Three nested loops.
    # Loop 1 (k): The "Detour" city. We check if routing our path through 'k' is faster.
    for k in range(V):
        # Loop 2 (i): The "Starting" city.
        for i in range(V):
            # Loop 3 (j): The "Destination" city.
            for j in range(V):
                
                # The big question: Is the path from i->k plus the path from k->j 
                # SHORTER than the direct path we currently have from i->j?
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    
                    # If the detour is faster, update our table with the new shorter distance!
                    dp[i][j] = dp[i][k] + dp[k][j]
                    
    # Return the fully optimized matrix
    return dp


# ==========================================
# 2. GRAPH GENERATOR (The Map Maker)
# ==========================================

def generate_graphs(V, density):
    # Create a 2D Matrix full of Infinities (for Floyd-Warshall)
    matrix = [[math.inf] * V for _ in range(V)]
    
    # Create an empty Adjacency List (for Dijkstra)
    adj_list = {i: [] for i in range(V)}
    
    # Loop through every possible pair of cities (i to j)
    for i in range(V):
        # The distance from any city to itself is exactly 0
        matrix[i][i] = 0  
        
        for j in range(V):
            # 1. Ensure we aren't connecting a city to itself (i != j)
            # 2. Roll a random decimal between 0 and 1. If it's less than our target density, we build a road!
            if i != j and random.random() < density:
                
                # Pick a random physical length/cost for this road (between 1 and 50)
                weight = random.randint(1, 50)  
                
                # Add this road to the Matrix format
                matrix[i][j] = weight
                
                # Add this exact same road to the List format
                adj_list[i].append((j, weight))
                
    # Return both perfectly identical maps so the algorithms have a fair race
    return adj_list, matrix
