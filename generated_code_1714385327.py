import sys

class Node:
    def __init__(self, val, g_cost=0, h_cost=0, parent=None):
        self.val = val
        self.g_cost = g_cost  # cost from start to current node
        self.h_cost = h_cost  # heuristic cost from current node to goal
        self.parent = parent  # parent node
        self.neighbors = []   # list of neighboring nodes

    def f_cost(self):
        return self.g_cost + self.h_cost

    def distance_to(self, neighbor):
        # Assuming some distance calculation method between nodes
        return 1  # For simplicity, assuming all distances as 1

class AStar:
    def __init__(self):
        pass

    def find_path(self, start, goal):
        open_set = [start]
        closed_set = []

        while open_set:
            current = open_set[0]
            for node in open_set:
                if node.f_cost() < current.f_cost() or (node.f_cost() == current.f_cost() and node.h_cost < current.h_cost):
                    current = node

            open_set.remove(current)
            closed_set.append(current)

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = current.parent
                return path[::-1]

            for neighbor in current.neighbors:
                if neighbor in closed_set:
                    continue

                tentative_g_score = current.g_cost + current.distance_to(neighbor)
                if neighbor not in open_set:
                    open_set.append(neighbor)
                elif tentative_g_score >= neighbor.g_cost:
                    continue

                neighbor.parent = current
                neighbor.g_cost = tentative_g_score
                neighbor.h_cost = neighbor.distance_to(goal)

        return None

# Example 1
start = Node("Start", g_cost=0, h_cost=5)  # start node
goal = Node("Goal")  # goal node
node1 = Node("Node 1", g_cost=2, h_cost=3)
node2 = Node("Node 2", g_cost=4, h_cost=2)
node3 = Node("Node 3", g_cost=5, h_cost=1)

start.neighbors = [node1, node2]
node1.neighbors = [start, node2, node3]
node2.neighbors = [start, node1, node3, goal]
node3.neighbors = [node1, node2, goal]
goal.neighbors = [node2, node3]

astar = AStar()
path = astar.find_path(start, goal)

if path:
    print("Path found:")
    for node in path:
        print(node.val)
else:
    print("No path found.")

# Example 2
start = Node("Start", g_cost=0, h_cost=10)  # start node
goal = Node("Goal")  # goal node
node1 = Node("Node 1", g_cost=1, h_cost=8)
node2 = Node("Node 2", g_cost=2, h_cost=7)
node3 = Node("Node 3", g_cost=3, h_cost=6)
node4 = Node("Node 4", g_cost=4, h_cost=5)
node5 = Node("Node 5", g_cost=5, h_cost=4)
node6 = Node("Node 6", g_cost=6, h_cost=3)
node7 = Node("Node 7", g_cost=7, h_cost=2)
node8 = Node("Node 8", g_cost=8, h_cost=1)

start.neighbors = [node1, node2]
node1.neighbors = [start, node2, node3]
node2.neighbors = [start, node1, node3, node4]
node3.neighbors = [node1, node2, node4, node5]
node4.neighbors = [node2, node3, node5, node6]
node5.neighbors = [node3, node4, node6, node7]
node6.neighbors = [node4, node5, node7, node8]
node7.neighbors = [node5, node6, node8, goal]
node8.neighbors = [node6, node7, goal]
goal.neighbors = [node7, node8]

astar = AStar()
path = astar.find_path(start, goal)

if path:
    print("Path found:")
    for node in path:
        print(node.val)
else:
    print("No path found.")