from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    """
    This class represents a directional weighted graph.
    Each vertex in the graph is from the type of node_data and
    every edge has a positive weight and direction.
    The class supports several operations applicable on a graph,such as:
    adding and removing a vertex or an edge, getting a dictionary of the edges which
    getting out or in of a vertex, getting all the vertexes in the graph, the number of
    the nodes or the edges in the graph, or the number of the changes which has been made in the graph.
    """

    def __init__(self):
        self._vertexes = {}
        self._MC = 0
        self._edges_size = 0

    def __repr__(self):
        """"
        This function is a simple reper function of this graph.
        The function provides the number of the the vertexes and the edges which in the graph.
        @return: a string with the number of the the vertexes and the edges which in the graph.
        """
        return f"Graph |V|:{len(self._vertexes)} |E|: {self._edges_size}"

    def __contains__(self, item: int):
        """
        This function checks if the given key in one of the vertexes of this graph.
        :param item: the node's key.
        :return: True if the node which associated with this key is in the graph, False otherwise.
        """
        for i in self._vertexes.keys():
            if i == item:
                return True
        return False

    def get_all_v(self) -> dict:
        """
        This function returns a dictionary of all the nodes in the Graph,
        each node is represented using a pair (key, node_data).
        @return: The dictionary of all the nodes in the graph.
        """
        return self._vertexes

    def v_size(self) -> int:
        """
        This function returns the number of vertexes in this graph.
        @return: The number of vertexes in this graph
        """
        return len(self._vertexes)

    def e_size(self) -> int:
        """
        This function returns the number of edges in this graph.
        @return: The number of edges in this graph.
        """
        return self._edges_size

    def get_mc(self) -> int:
        """
        This function returns the current version of this graph,
        on every change in the graph state - the MC is increased.
        @return: The current version of this graph.
        """
        return self._MC

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        This function adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        """
        if not self._vertexes.__contains__(node_id):
            self._vertexes[node_id] = NodeData(node_id, pos)
            self._MC += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        """
        This function removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        """
        if self._vertexes.__contains__(node_id):
            srcs_of_this_node = self._vertexes.get(node_id).get_dest()
            for i in srcs_of_this_node.keys():
                self._vertexes.get(i).remove_src(node_id)
                self._edges_size -= 1
            self._vertexes.pop(node_id)
            self._MC += 1
            return True
        else:
            return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        This function adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        """
        if self._vertexes.__contains__(id1) and self._vertexes.__contains__(id2):
            if not self._vertexes.get(id1).has_dest(id2):
                self._vertexes.get(id1).add_dest(id2, weight)
                self._vertexes.get(id2).add_src(id1, weight)
                self._edges_size += 1
                self._MC += 1
                return True
            return False
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        This function removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if self._vertexes.__contains__(node_id1) and self._vertexes.__contains__(node_id2):
            if self._vertexes.get(node_id1).has_dest(node_id2):
                self._vertexes.get(node_id1).remove_dest(node_id2)
                self._vertexes.get(node_id2).remove_src(node_id1)
                self._edges_size -= 1
                self._MC += 1
                return True
            return False
        return False

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        This function returns a dictionary of all the nodes connected from node_id ,
        each node is represented using a pair (key,weight).
        @param id1: the node_id which the edges in the dictionary

        """
        if self._vertexes.__contains__(id1):
            return self._vertexes.get(id1).get_dest()
        else:
            return {}

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
        """
        if self._vertexes.__contains__(id1):
            return self._vertexes.get(id1).get_src()
        else:
            return {}

    def __eq__(self, other):
        if not(isinstance(other, DiGraph)) or (other is None):
            return False
        else:
            if (self.e_size() != other.e_size()) or (self.v_size() != other.v_size()):
                return False
            else:
                for i in self._vertexes.keys():
                    if not other.__contains__(i):
                        return False
                    else:
                        for k, v in self.all_out_edges_of_node(i).items():
                            if not other.get_all_v().get(i).has_dest(k, v):
                                return False
        return True
