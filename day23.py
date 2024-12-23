import networkx as nx
import matplotlib.pyplot as plt 
import numpy as np
N=70
def read_tuples_from_file(file_path,sep=','):
    """
    Reads a text file and converts each line into a tuple of integers.
    
    :param file_path: Path to the text file
    :return: List of tuples containing integers
    """
    with open(file_path, 'r') as file:
        tuples_list = [line.strip().split(sep) for line in file if line.strip()]
    return tuples_list

filename = "day23.txt"
computers = read_tuples_from_file(filename,sep='-')
nodes = np.unique([np.unique(l) for l in computers])

G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc

G.add_nodes_from(nodes )
G.add_edges_from(computers)
 # Generate a layout for nodes
pos = nx.spring_layout(G, seed=42)  # spring layout for aesthetics
# Draw the graph
plt.figure(figsize=(10, 10))
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='skyblue', edgecolors='black')
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=14, font_color='black')

cliques = list(nx.find_cliques(G))
largest_clique = max(cliques, key=len)

# Highlight the largest clique
nx.draw_networkx_nodes(G, pos, nodelist=largest_clique, node_size=800, node_color='orange', edgecolors='red')
nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u in largest_clique for v in largest_clique if G.has_edge(u, v)], width=3, edge_color='red')


# Add a title
plt.title("DAY 23 AOC 2024", fontsize=16, fontweight='bold')
plt.axis('off')  # Turn off the axes
plt.show()

triangles = [triangle for triangle in nx.enumerate_all_cliques(G) if len(triangle) == 3]

def find_computers(computers,letter='t'):
    return [ l for l in computers if l[0].startswith(letter) or l[1].startswith(letter) or l[2].startswith(letter)]

t_computers = find_computers(triangles)
print(t_computers)
print(len(t_computers))

# Use the built-in function to find the largest clique
largest_clique = nx.algorithms.clique.find_cliques(G)
    
 # Find the clique with the maximum size
print(','.join( sorted(max(largest_clique, key=len))))