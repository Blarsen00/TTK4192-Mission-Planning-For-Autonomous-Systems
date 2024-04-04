from util import Graph
import numpy as np
import matplotlib.pyplot as plt

# You should only need to use the following functions to implement dijkstra:
# Graph(path_to_map) # path_to_map can, for instance, be 'maps/map1.png'
# graph.get_list_of_nodes()
# graph.get_neighbors(node)
# graph.get_start_node()
# graph.get_goal_node()

# For visualizing the algorithm use the following functions:
# graph.add_visited_node(node) # Use this when you are visiting a new node to update the visualization
# graph.add_shortest_path(path) # Use this to visualize the shortest path after you have found it.

def dijkstra(graph):
    # Here you need to implement Dijkstra's algorithm. Remember to modify it to stop when the shortest path to the
    # goal node has been found. The implementation should return the path from start to goal, in the form of a
    # sequential list of nodes in the path.

    manhattan_distance = lambda pos1, pos2: abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    euclidean_distance = lambda pos1, pos2: np.linalg.norm(np.array(pos2) - np.array(pos1)) 

    start = graph.get_start_node()
    goal = graph.get_goal_node()

    # Set all nodes' distances, except start node, to infinity
    not_visited = {x : np.infty for x in graph.get_list_of_nodes()}
    not_visited[tuple(start)] = 0
    not_visited = dict(sorted(not_visited.items(), key=lambda x: x[1]))

    # Make a tree in order to find the path
    tree : dict = {x : None for x in not_visited.keys()}

    while len(not_visited) > 0:
        current_node = min(not_visited, key=lambda k: not_visited[k])
        current_distance = not_visited.pop(current_node)
        graph.add_visited_node(current_node)
        
        if current_node == tuple(goal):
            path = [goal]
            print(f"Found the distance to be {current_distance}")
            
            while tree[current_node] != None:
                parent = tree[current_node]
                path.insert(0, parent)
                current_node = parent
            
            path.insert(0, start)
            graph.add_shortest_path(path)
            return path 
        
        for neighbor in graph.get_neighbors(current_node):
            # Skip visited nodes
            if neighbor not in not_visited:
                continue

            # Update the tree
            tree[neighbor] = current_node

            d = not_visited[neighbor]
            # Pick whichever you prefer to calculate distance
            # not_visited[neighbor] = min(d, current_distance + manhattan_distance(current_node, neighbor))
            not_visited[neighbor] = min(d, current_distance + euclidean_distance(current_node, neighbor))


    print("Couldn't find a solution :(")
    raise NotImplementedError


if __name__ == "__main__":
    maps = [f'maps/map{x}.png' for x in range(1,6)]
    for i, map in enumerate(maps):
        print(f'Calculating for map {i+1}...')
        graph = Graph(map)
        path = dijkstra(graph)
        graph.add_shortest_path(path)

        graph.fig.suptitle(f'Dijkstra for map {i+1}')
        graph.fig.tight_layout()
        graph.fig.savefig(f'SolutionMap{i+1}.pdf')

    # graph = Graph('maps/map2.png')
    # path = dijkstra(graph)

    # graph.add_shortest_path(path)
