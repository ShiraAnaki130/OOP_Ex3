from src import GraphInterface
from NodeData import NodeData

MC: int = 0
edges_size: int = 0


class DiGraph:

    def __init__(self):
        self._vertexes = {}

    def __repr__(self):
        return f"DiGraph vertexes:{self._vertexes.keys()}"

    def __contains__(self, item: int):
        for i in self._vertexes.keys():
            if i == item:
                return True
        return False

    def get_all_v(self) -> dict:
        return self._vertexes

    def v_size(self) -> int:
        return len(self._vertexes)

    def e_size(self) -> int:
        return edges_size

    @property
    def get_mc(self) -> int:
        return MC

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if not self._vertexes.__contains__(node_id):
            self._vertexes[node_id] = NodeData(self, node_id, pos)
            global MC
            MC += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if self._vertexes.__contains__(node_id):
            srcs_of_this_node = self._vertexes.get(node_id).get_dest()
            for i in srcs_of_this_node.keys():
                self._vertexes.get(i).remove_src(node_id)
                global edges_size
                edges_size -= 1
            self._vertexes.pop(node_id)
            global MC
            MC += 1
            return True
        else:
            return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self._vertexes.__contains__(id1) and self._vertexes.__contains__(id2):
            if not self._vertexes.get(id1).has_dest(id2):
                self._vertexes.get(id1).add_dest(id2, weight)
                self._vertexes.get(id2).add_src(id1, weight)
                global edges_size
                edges_size += 1
                global MC
                MC += 1
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
                global edges_size
                edges_size -= 1
                global MC
                MC += 1
                return True
            return False
        return False

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        This function returns a dictionary of all the nodes connected from node_id ,
        each node is represented using a pair (key,weight).
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

