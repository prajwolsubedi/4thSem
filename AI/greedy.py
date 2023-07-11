def greedy_search(graph, start, goal):
    visited = []
    path = [start]
    current = start
    
    while current != goal:
        neighbors = graph[current]
        best_neighbor = None
        best_distance = float('inf')
        
        for neighbor, distance in neighbors.items():
            if neighbor not in visited and distance < best_distance:
                best_neighbor = neighbor
                best_distance = distance
        
        if best_neighbor is None:
            print("Goal cannot be reached!")
            return None
        
        visited.append(current)
        path.append(best_neighbor)
        current = best_neighbor
    
    return path


# Example usage
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'D': 6, 'E': 4},
    'D': {'F': 8},
    'E': {'F': 3},
    'F': {}
}

start_node = 'A'
goal_node = 'F'

result = greedy_search(graph, start_node, goal_node)

if result is not None:
    print(f"Path from {start_node} to {goal_node}: {result}")
