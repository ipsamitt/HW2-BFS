# write tests for bfs
from search import graph
import pytest
import networkx as nx

def test_bfs_traversal():

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


    Be sure that your code can handle possible edge cases, e.g.:
    running bfs traversal on an empty graph
    running bfs traversal on an unconnected graph
    running bfs from a start node that does not exist in the graph
    running bfs search for an end node that does not exist in the graph
    any other edge cases you can think of
    """
    
    new_graph = graph.Graph('data/citation_network.adjlist')
    bfs_tree = nx.bfs_tree(new_graph.graph, source="Luke Gilbert")
    
    new_graph = graph.Graph('data/citation_network.adjlist')
    whole_path = list(nx.bfs_tree(new_graph.graph, source="Luke Gilbert").nodes())
    target_index = whole_path.index("Tony Capra")
    ground_truth = whole_path[:target_index+1]
    assert((new_graph.bfs("Luke Gilbert", end="Tony Capra")) == (list(ground_truth)))


#searching for end node that doesn't exist in the graph
    assert((new_graph.bfs("Luke Gilbert", end="Abul Abbas")) == None)
    
    
    
