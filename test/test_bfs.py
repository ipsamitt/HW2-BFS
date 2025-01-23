# write tests for bfs
from search import graph
import pytest
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    new_graph = graph.Graph('data/tiny_network.adjlist')
    assert(len(new_graph.bfs("Luke Gilbert", end=None))  == 30)
    ground_truth = nx.bfs_tree(new_graph.graph, source="Luke Gilbert").nodes()
    assert((new_graph.bfs("Luke Gilbert", end=None)) == (list(ground_truth)))

    assert(len(new_graph.bfs("Atul Butte", end=None))  == 30)
    ground_truth = nx.bfs_tree(new_graph.graph, source="Atul Butte").nodes()
    assert((new_graph.bfs("Atul Butte", end=None)) == (list(ground_truth)))
    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    
    new_graph = graph.Graph('data/citation_network.adjlist')

    
    
    pass
