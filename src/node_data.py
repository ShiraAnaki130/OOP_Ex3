class node_data:
    """This abstract class represents an interface of node (vertex) in a directional
    weighted graph.
    """

    def as_dict_node(self):
        """
        This function creates a dictionary of this node.
        @return: the dictionary of this node.
        """
        raise NotImplementedError

    def __repr__(self):
        """"
        This function is a simple reper function of this node.
        The function provides the number of the the edges which getting out and in of this node.
        @return: a string with the number of the the edges which getting out and in of this node.
        """
        raise NotImplementedError

    def add_dest(self, dest: int, weight: float):
        """
        This function adds another pair of (key, weight) which represent a new edge
        in which this node is the edge's source.
        :param dest: the new edge's destination.
        :param weight: the weight of the new edge.
        :return: None
        """
        raise NotImplementedError

    def add_src(self, src: int, weight: float):
        """
        This function adds another pair of (key, weight) which represent a new edge
        in which this node is the edge's destination.
        :param src: the new edge's source.
        :param weight: the weight of the new edge.
        :return: None
        """
        raise NotImplementedError

    def has_dest(self, dest: int) -> bool:
        """
        This function checks if there is an edge in which this node is the edge's source and
        given key is the edge's destination.
        :param dest: the given key destination.
        :return: True if there the edge is exist, or False otherwise.
        """
        raise NotImplementedError

    def has_src(self, src: int) -> bool:
        """
        This function checks if there is an edge in which this node is the edge's destination
        and the given key is the edge's source.
        :param src: the edge's source.
        :return: True if this edge is exist, or False otherwise.
        """
        raise NotImplementedError

    def remove_dest(self, dest: int) -> bool:
        """
        This function removes the given dest from the dest dictionary.
        :param dest: the destination key to remove.
        :return: True if the dest removed, or False otherwise.
        """
        raise NotImplementedError

    def remove_src(self, src: int) -> bool:
        """
        This function removes the given src from the src dictionary.
        :param src: the source key to remove.
        :return: True if the source removed, or False otherwise.
        """
        raise NotImplementedError

    def get_dest(self) -> dict:
        """
        This function returns a dictionary (key, weight) of all the edges in which this node is the
        edges's source.
        :return: the dictionary of all the edges in which this node is the edges's source.
        """
        raise NotImplementedError

    def get_src(self) -> dict:
        """
        This function returns a dictionary (key, weight) of all the edges in which this node is the
        edges's destination.
        :return: the dictionary of all the edges in which this node is the edges's destination.
        """
        raise NotImplementedError

    def get_weight(self, dest: int) -> float:
        """
        This function returns the weight of the edge in which this node is the edge's source
        and the given key is the edge's destination.
        :param dest: given key destination.
        :return: the weight of the edge which this node is the source and the given
        key is the edge's destination.
        """
        raise NotImplementedError

    def get_key(self) -> int:
        """
        This function returns this node's key.
        :return: the key of this node.
        """
        raise NotImplementedError

    def set_key(self, id: int):
        """
        This function sets a new key to this node.
        :param id: the new key.
        """
        raise NotImplementedError

    def get_pos(self) -> tuple:
        """
        This function returns the position of this node.
        :return: the position of this node: 3 coordinates tuple, or Node(default case) .
        """
        raise NotImplementedError

    def set_pos(self, pos: tuple):
        """
        This function sets the position of the node.
        :param pos: tuple of the coordinates, or None(default case).
        """
        raise NotImplementedError

    def getWeight(self) -> float:
        """
        This function returns the node's weight.
        :return: the weight of the node.
        """
        raise NotImplementedError

    def set_weight(self, weight: float):
        """
        This function sets a new weight for this node.
        :param weight: the new weight.
        """
        raise NotImplementedError

    def get_tag(self) -> int:
        """
        This function returns the node's tag.
        :return: the tag of the node.
        """
        raise NotImplementedError

    def set_tag(self, tag: int):
        """
        This function sets a new tag to this node.
        :param tag: the new tag.
        """
        raise NotImplementedError

    def get_info(self) -> str:
        """
        This function returns the info of this node.
        :return: the info associated with this node.
        """
        raise NotImplementedError

    def set_info(self, info: str):
        """
        This function sets new info to this node.
        :param info: the new info.
        """
        raise NotImplementedError
