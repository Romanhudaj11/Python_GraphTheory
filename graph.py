# GF = (V, E)

# we import a data type called 'namedtuple' 
# namedtuple = tuple + give names to their components 
from collections import namedtuple 

# network = graph (let's us visualize graphs)
from pyvis.network import Network

# nametuple(# name of type, iterable containing field names (components: vertcies and edges), boolean: is_directed)
Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])

# Adjacency List: 
#  easier to work with

def adjacency_dict(graph):
  """
    input: graph
    output: adjacency list representation of the graph
  """
  # dictiorary {node : []}
  #   key = node
  #   value = [set of edges]
  adj = {node : [] for node in graph.nodes}

  #Go through every edge to build 'adj'
  for edge in graph.edges: 
    node1, node2 = edge[0], edge[1]
    adj[node1].append(node2) # add node2 to node1 adj-list
    if not graph.is_directed: 
      adj[node2].append(node1) # add node1 to node2 adj-list
  
  return adj


# Adjaceny matrix
#   represents adjacency as a 2D matrix 
#

def adjacency_matrix(graph):
  """
    input: graph
    output: adjacency matrix representation of the graph
    Assume: nodes are defined as integers in range(len(graph.nodes))
  """
  adj = [[0 for node in graph.nodes] for node in graph.nodes]
  for edge in graph.edges: 
    node1, node2 = edge[0], edge[1] 
    adj[node1][node2] += 1
    if not graph.is_directed: 
      adj[node2][node1] += 1
  return adj 

"""
Adjacency List: 
  - can handle arbitrary hashable nodes
  - good for graphs with few edges, uses less memory 
Adjacency Matrix: 
  - Only works for graphs whose nodes are integers
  - Not a good choice for sparse graphs, uses most memory 
"""

# visualize graphs from nametuple Type 

def show(graph, output_filename): 
  """
    Input: a graph & a filename to save
    Output: HTML file locally containing a visualization of the graph
  """
  g = Network(directed=graph.is_directed)
  # add nodes to g
  g.add_nodes(graph.nodes) # pass the list of nodes
  g.add_edges(graph.edges) # pass list of edges 
  g.show(output_filename)  # visualize the graph (creates html file)
  return g                 # return 
