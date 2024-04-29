class Node:
    def __init__(self, val):
        self.val = val
        self.g_cost = 0
        self.h_cost = 0
        self.parent = None
        self.neighbors = []

    def f_cost(self):
        return self.g_cost + self.h_cost

    def distance_to(self, neighbor):
        return 1


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


# Hard Coded Example
start = Node("Start")
goal = Node("Goal")
node1 = Node("Node 1")
node2 = Node("Node 2")
node3 = Node("Node 3")

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