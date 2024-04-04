from util import Graph
import numpy as np
import matplotlib.pyplot as plt

# You should only need to use the following functions to implement A*:
# Graph(path_to_map) # path_to_map can, for instance, be 'maps/map1.png'
# graph.get_list_of_nodes()
# graph.get_neighbors(node)
# graph.get_start_node()
# graph.get_goal_node()

# For visualizing the algorithm use the following functions:
# graph.add_visited_node(node) # Use this when you are visiting a new node to update the visualization
# graph.add_shortest_path(path) # Use this to visualize the shortest path after you have found it.

def a_star(graph, heuristic_function=None):
    # Here you need to implement A*. The implementation should return the path from start to goal, in the form of a
    # sequential list of nodes in the path.
    manhattan_distance = lambda pos1, pos2: abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    euclidean_distance = lambda pos1, pos2: np.linalg.norm(np.array(pos2) - np.array(pos1)) 
    
    if heuristic_function == None:
        heuristic_function = lambda x: manhattan_distance(x, goal)
        # heuristic_function = euclidean_distance

    start = graph.get_start_node()
    goal = graph.get_goal_node()

    open_set = [tuple(start)]
    g = {x : np.infty for x in graph.get_list_of_nodes()}
    g[tuple(start)] = 0

    f = g.copy()
    f[tuple(start)] = heuristic_function(start)

    tree = {x : None for x in graph.get_list_of_nodes()}

    while len(open_set) > 0:
        # Current node is the node with the lowest score
        current_node = open_set.pop(0)
        graph.add_visited_node(current_node)
        
        if current_node == tuple(goal):
            path = [goal]
            print(f"Found the distance to be {g[current_node]}")
            
            while tree[current_node] != None:
                parent = tree[current_node]
                path.insert(0, parent)
                current_node = parent
            
            path.insert(0, start)
            graph.add_shortest_path(path)
            return path 
        
        for neighbor in graph.get_neighbors(current_node):
            current_g = g[neighbor]
            # Pick whichever you prefer to calculate distance
            potential_g = g[current_node] + manhattan_distance(current_node, neighbor)
            # potential_g = g[current_node] + euclidean_distance(current_node, neighbor)
            d = min(current_g, potential_g)

            if potential_g < current_g:
                tree[neighbor] = current_node
                
                if neighbor not in open_set:
                    open_set.append(neighbor)

            # Update the scores
            g[neighbor] = d
            f[neighbor] = d + heuristic_function(neighbor)
        
        # Sort the list, so popping the first element gives the lowest score
        open_set.sort(key=lambda x:f[x])


    print("Couldn't find a solution :(")
    return None

if __name__ == "__main__":
    maps = [f'maps/map{x}.png' for x in range(1,6)]
    for i, map in enumerate(maps):
        print(f'Calculating for map {i+1}...')
        graph = Graph(map)
        path = a_star(graph)
        graph.add_shortest_path(path)

        graph.fig.suptitle(f'A* for map {i+1}')
        graph.fig.tight_layout()
        graph.fig.savefig(f'SolutionMap{i+1}.pdf')
    # graph = Graph('maps/map4.png')
    # path = a_star(graph, heuristic_function=None)

    # graph.add_shortest_path(path)
