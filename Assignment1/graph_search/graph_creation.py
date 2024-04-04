import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Start edges
G.add_edge('S', 'A', weight=210) 

# A edges
G.add_edge('A', 'B', weight=220)
G.add_edge('A', 'D', weight=65) 

# B edges
G.add_edge('B', 'C', weight=75) 

# C edges
G.add_edge('C', 'F', weight=560) 
G.add_edge('C', 'D', weight=250)

# D edges
G.add_edge('D', 'E', weight=720)

# E edges
G.add_edge('E', 'G', weight=150)
G.add_edge('E', 'K', weight=750)

# F edges
G.add_edge('F', 'G', weight=340)
G.add_edge('F', 'I', weight=180)

# G edges
G.add_edge('G', 'H', weight=70)

# H edges
G.add_edge('H', 'I', weight=310)
G.add_edge('H', 'J', weight=350)

# I edges
G.add_edge('I', 'L', weight=400)

# J edges
G.add_edge('J', 'Goal', weight=120)
G.add_edge('J', 'K', weight=140)

# K edges
G.add_edge('K', 'L', weight=730)

# L edges
G.add_edge('L', 'Goal', weight=410, color='green')

# Calculate the shortest path and print the results
print(nx.shortest_path(G, 'S', 'Goal', weight='weight'), nx.shortest_path_length(G, 'S', 'Goal', weight='weight'))


