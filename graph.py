### graph.py ####

class Graph(object):
    """
    Represents a directed graph.
    """

    def __init__(self):
        """
        Initializes the Graph to an empty graph with no nodes or edges.
        """
        self._nodes = []
        self._edges = []

    def add_node(self, node):
        """
        If node is already in the graph, returns False and does not modify the graph.
        Otherwise, adds node to the graph and returns True.
        """
        if node in self._nodes:
            return False
        else:
            self._nodes.append(node)

    def has_node(self, node):
        """
        Returns True if node is a node in the graph.
        """
        return self._nodes.get(node)


    def add_edge(self, node1, node2):
        """
        Requires: node1 and node2 are nodes in self.
        Modifies: self
        Adds an edge from node1 to node2 to self.
        """
        if node1 in self._nodes and node2 in self._nodes:
            self._edges.append((node1,node2))

    def get_nodes(self):
        """
        Returns a frozenset containing the nodes in the graph.
        """
        return frozenset(self._nodes)

    def get_outlinks(self, node):
        """
        Requires: node is a node in self.
        Returns a frozenset of the nodes to which node is connected.
        """
        if node in self._nodes:
            connections = []
            for edge in self._edges:
                if edge[0] == node:
                    connections.append(edge[1])
            return frozenset(connections)

    def get_inlinks(self, target):
        """
        Requires: node is a node in self.
        Returns a set of the nodes that are connected by an edge to node.
        """
        if target in self._nodes:
            inlinks = []
            for edge in self._edges:
                if edge[1] == target:
                    inlinks.append(edge[0])
            return frozenset(inlinks)
    
    def __str__(self):
        """
        Returns a string representation of the graph. 
        """
        return "nodes: " + str(self._nodes) + "; edges: " + str(self._edges)