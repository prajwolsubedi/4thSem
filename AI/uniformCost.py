from queue import PriorityQueue

# Define a Node class to represent the states in the search space


class Node:
    def __init__(self, state, cost=0):
        self.state = state
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(Node(start, 0))

    explored = set()

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        if current_state == goal:
            return current_node.cost

        explored.add(current_state)

        for neighbor, neighbor_cost in graph[current_state]:
            if neighbor not in explored:
                frontier.put(Node(neighbor, current_node.cost + neighbor_cost))

    return None


# Example usage
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3)],
    'D': [('E', 2)],
    'E': []
}

start_state = 'A'
goal_state = 'E'

path_cost = uniform_cost_search(graph, start_state, goal_state)
if path_cost is not None:
    print("Optimal path cost:", path_cost)
else:
    print("Goal state is not reachable.")
