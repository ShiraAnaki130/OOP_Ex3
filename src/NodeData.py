from src.node_data import node_data


class NodeData(node_data):

    def __init__(self, _id: int, _pos: tuple = None, weight: float = 0.0, tag: int = 0, info: str = "f"):
        """
        This function creates a new node_data with unique id, weight, position, tag, and info.
        Each node_data has a dictionary 'dest' for the edges in which this node is the source node
        and dictionary 'src' of the edges in which this node is the destination node.
        :param _id : key of the node
        :param _pos: 3 coordinates tuple, default: None.
        :param weight: float weight, default: 0.0.
        :param tag: int tag, default: 0.
        :param info: string info, default: "f".
        """
        self.pos = _pos
        self.id = _id
        self._weight = weight
        self._tag = tag
        self._info = info
        self._src = {}
        self._dest = {}

    def as_dict_node(self):
        """
        This function creates a dictionary of this node.
        @return: the dictionary of this node.
        """
        node_dict = self.__dict__
        return node_dict

    def __repr__(self):
        """"
        This function is a simple reper function of this node.
        The function provides the number of the the edges which getting out and in of this node.
        @return: a string with the number of the the edges which getting out and in of this node.
        """
        return f"{self.id}: |edges out|: {len(self._dest)} |edges in|: {len(self._src)}"

    def add_dest(self, dest: int, weight: float):
        """
        This function adds another pair of (key, weight) which represent a new edge
        in which this node is the edge's source.
        :param dest: the new edge's destination.
        :param weight: the weight of the new edge.
        :return: None
        """
        if dest != self.id:
            self._dest[dest] = weight

    def has_dest(self, dest: int, weight: float = None) -> bool:
        """
        This function checks if there is an edge in which this node is the edge's source and
        given key is the edge's destination.
        :param dest: the given key destination.
        :return: True if there the edge is exist, or False otherwise.
        """
        if dest != self.id:
            for k, v in self._dest.items():
                if weight is None:
                    if k == dest:
                        return True
                else:
                    if k == dest and v == weight:
                        return True
        return False

    def has_src(self, src: int) -> bool:
        """
        This function checks if there is an edge in which this node is the edge's destination
        and the given key is the edge's source.
        :param src: the edge's source.
        :return: True if this edge is exist, or False otherwise.
        """
        if src != self.id:
            for i in self._src.keys():
                if i == src:
                    return True
        return False

    def remove_dest(self, dest: int) -> bool:
        """
        This function removes the given dest from the dest dictionary.
        :param dest: the destination key to remove.
        :return: True if the dest removed, or False otherwise.
        """
        if self.has_dest(dest):
            self._dest.pop(dest)
            return True
        return False

    def remove_src(self, src: int) -> bool:
        """
        This function removes the given src from the src dictionary.
        :param src: the source key to remove.
        :return: True if the source removed, or False otherwise.
        """
        if self.has_src(src):
            self._src.pop(src)
            return True
        return False

    def add_src(self, src: int, weight: float):
        """
        This function adds another pair of (key, weight) which represent a new edge
        in which this node is the edge's destination.
        :param src: the new edge's source.
        :param weight: the weight of the new edge.
        :return: None
        """
        if src != self.id:
            self._src[src] = weight

    def get_dest(self) -> dict:
        """
        This function returns a dictionary (key, weight) of all the edges in which this node is the
        edges's source.
        :return: the dictionary of all the edges in which this node is the edges's source.
        """
        return self._dest

    def get_src(self) -> dict:
        """
        This function returns a dictionary (key, weight) of all the edges in which this node is the
        edges's destination.
        :return: the dictionary of all the edges in which this node is the edges's destination.
        """
        return self._src

    def getWeight(self, dest: int) -> float:
        """
        This function returns the weight of the edge in which this node is the edge's source
        and the given key is the edge's destination.
        :param dest: given key destination.
        :return: the weight of the edge which this node is the source and the given
        key is the edge's destination.
        """
        return self._dest.get(dest)

    def get_key(self) -> int:
        """
        This function returns this node's key.
        :return: the key of this node.
        """
        return self.id

    def set_key(self, id: int):
        """
        This function sets a new key to this node.
        :param id: the new key.
        """
        self.id = id

    def get_pos(self) -> tuple:
        """
        This function returns the position of this node.
        :return: the position of this node: 3 coordinates tuple, or Node(default case) .
        """
        return self.pos

    def set_pos(self, pos: tuple):
        """
        This function sets the position of the node.
        :param pos: tuple of the coordinates, or None(default case).
        """
        self.pos = pos

    def get_weight(self) -> float:
        """
        This function returns the node's weight.
        :return: the weight of the node.
        """
        return self._weight

    def set_weight(self, weight: float):
        """
        This function sets a new weight for this node.
        :param weight: the new weight.
        """
        self._weight = weight

    def get_tag(self) -> int:
        """
        This function returns the node's tag.
        :return: the tag of the node.
        """
        return self._tag

    def set_tag(self, tag: int):
        """
        This function sets a new tag to this node.
        :param tag: the new tag.
        """
        self._tag = tag

    def get_info(self) -> str:
        """
        This function returns the info of this node.
        :return: the info associated with this node.
        """
        return self._info

    def set_info(self, info: str):
        """
        This function sets new info to this node.
        :param info: the new info.
        """
        self._info = info
