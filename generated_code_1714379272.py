# Node class stores the node's value, cost from start (g_cost), heuristic cost to goal (h_cost), parent node, and neighbors.
class Node:
    def __init__(self, val, g_cost=0, h_cost=0, parent=None):
        self.val = val
        self.g_cost = g_cost  # cost from start to current node
        self.h_cost = h_cost  # heuristic cost from current node to goal
        self.parent = parent  # parent node
        self.neighbors = []  # list of neighboring nodes

    # Calculates the f_cost (total cost) of the node.
    def f_cost(self):
        return self.g_cost + self.h_cost

    # Calculates the distance between the node and a neighboring node.
    def distance_to(self, neighbor):
        # Assuming some distance calculation method between nodes
        return 1  # For simplicity, assuming all distances as 1


# AStar class implements the A* pathfinding algorithm.
class AStar:
    def __init__(self):
        pass

    # Finds the path from the start node to the goal node using the A* algorithm.
    def find_path(self, start, goal):
        open_set = [start]  # Nodes to be evaluated
        closed_set = []  # Nodes that have been evaluated

        # While there are nodes to be evaluated
        while open_set:
            # Get the node with the lowest f_cost from the open set
            current = open_set[0]
            for node in open_set:
                if node.f_cost() < current.f_cost() or (node.f_cost() == current.f_cost() and node.h_cost < current.h_cost):
                    current = node

            # Remove the current node from the open set and add it to the closed set
            open_set.remove(current)
            closed_set.append(current)

            # If the current node is the goal node, return the path from the start node to the goal node
            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = current.parent
                return path[::-1]

            # For each neighbor of the current node
            for neighbor in current.neighbors:
                # If the neighbor is in the closed set, skip it
                if neighbor in closed_set:
                    continue

                # Calculate the tentative g_cost of the neighbor
                tentative_g_score = current.g_cost + current.distance_to(neighbor)

                # If the neighbor is not in the open set or the tentative g_cost is lower than the neighbor's current g_cost
                if neighbor not in open_set or tentative_g_score < neighbor.g_cost:
                    # Update the neighbor's parent, g_cost, and h_cost
                    neighbor.parent = current
                    neighbor.g_cost = tentative_g_score
                    neighbor.h_cost = neighbor.distance_to(goal)

                    # If the neighbor is not in the open set, add it to the open set
                    if neighbor not in open_set:
                        open_set.append(neighbor)

        # If no path was found, return None
        return None


# Test case
def test():
    # Create nodes with values
    start = Node("Start", g_cost=0, h_cost=5)  # Start node
    goal = Node("Goal")  # Goal node
    node1 = Node("Node 1", g_cost=2, h_cost=3)
    node2 = Node("Node 2", g_cost=4, h_cost=2)
    node3 = Node("Node 3", g_cost=5, h_cost=1)

    # Set up neighbors
    start.neighbors = [node1, node2]
    node1.neighbors = [start, node2, node3]
    node2.neighbors = [start, node1, node3, goal]
    node3.neighbors = [node1, node2, goal]
    goal.neighbors = [node2, node3]

    # Run A* algorithm
    astar = AStar()
    path = astar.find_path(start, goal)

    # Print the result
    if path:
        print("Path found:")
        for node in path:
            print(node.val)
    else:
        print("No path found.")


# Run the test
test()