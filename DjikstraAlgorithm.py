import heapq

def dijkstra(graph, source):
    # Initialize distances with infinity and source with 0
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    # Min-priority queue: (distance, vertex)
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if we found a better path already
        if current_distance > distances[current_node]:
            continue
            
        # Relaxation step
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Example Input: Adjacency List
# graph = { 'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, ... }
graph = {
    '0': {'1': 4, '7': 8},
    '1': {'0': 4, '2': 8, '7': 11},
    '2': {'1': 8, '3': 7, '8': 2, '5': 4},
    '3': {'2': 7, '4': 9, '5': 14},
    '4': {'3': 9, '5': 10},
    '5': {'2': 4, '3': 14, '4': 10, '6': 2},
    '6': {'5': 2, '7': 1, '8': 6},
    '7': {'0': 8, '1': 11, '6': 1, '8': 7},
    '8': {'2': 2, '6': 6, '7': 7}
}

source_vertex = '0'
shortest_paths = dijkstra(graph, source_vertex)

print(f"Shortest distances from source {source_vertex}:")
for node, dist in shortest_paths.items():
    print(f"Vertex {node}: {dist}")