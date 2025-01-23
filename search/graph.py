import networkx as nx


class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def nodes(self):
        """
        Returns the nodes of the graph
        """
        return self.graph.nodes()
    
    def edges(self):
        """
        Returns the edges of the graph
        """
        return self.graph.edges()
    
    def bfs(self, start, end=None):

        # empty graph
        if len(self.graph.nodes()) == 0:
              raise Exception("Empty graph")
        
        # start node not in graph
        if start not in self.graph.nodes():
            raise Exception("Start node not in graph")

        
        #If there's no end node input, return a list nodes with the order of BFS traversal
        visited = []       

        if end is None:
            Q = []
            Q.append(start)
            visited.append(start)
            while len(Q) != 0:
                node = Q.pop(0)
                neighbors = list(self.graph.neighbors(node))
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        Q.append(neighbor)


        #If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        #If there is an end node input and a path does not exist, return None

        if end is not None:
            Q = []
            Q.append(start)
            visited.append(start)
            while len(Q) != 0:
                node = Q.pop(0)
                neighbors = list(self.graph.neighbors(node))
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        Q.append(neighbor)
                        if neighbor == end:
                            return visited
            
            return None
        
        return visited
    


