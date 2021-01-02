class NodeData:
    def __init__(self, id: int, pos: tuple = (0, 0, 0), weight: float = 0.0, tag: int = 0, info: str = "f"):
        """
        create new node data with unique id, weight, position, tag, and info.
        the node create dict dest for its edges it's the source node and dict src of its edges it's the destination node.
        :param id : key of the node
        :param pos: 3 coordinates tuple default (0.0,0.0,0.0)
        :param weight: float weight default 0.0
        :param tag: int tag default 0
        :param info: string info default "f"
        """
        self._pos = pos
        self._id = id
        self._weight = weight
        self._tag = tag
        self._info = info
        self._src = {}
        self._dest = {}

    def as_dict_node(self):
        """
        create dict of the node data param.
        """
        node_dict = self.__dict__
        return node_dict

    def __repr__(self):
        return f"{self._id}: |edges out|: {len(self._dest)} |edges in|: {len(self._src)}"

    def add_dest(self, dest: int, weight: float):
        """
        This function adds another node to be the destination of this node.
        :param dest: destination node to connect.
        :param weight: the weight of the edge.
        :return:
        """
        if dest != self._id:
            self._dest[dest] = weight

    def has_dest(self, dest: int) -> bool:
        """
        check if this node is source to edge with the given destination key.
        :param dest: the given destination.
        """
        if dest != self._id:
            for i in self._dest.keys():
                if i == dest:
                    return True
        return False

    def has_src(self, src: int) -> bool:
        """
          check if this node is destination to edge with the given source key.
          :param src: the given source.
        """
        if src != self._id:
            for i in self._src.keys():
                if i == src:
                    return True
        return False

    def remove_dest(self, dest: int) -> bool:
        """
        remove the given dest from the dest dict.
        :param dest: the destination to remove.
        :return: True if the dest removed False otherwise.
        """
        if self.has_dest(dest):
            self._dest.pop(dest)
            return True
        return False

    def remove_src(self, src: int) -> bool:
        """
           remove the given src from the src dict.
           :param src: the source to remove.
           :return: True if the source removed False otherwise.
        """
        if self.has_src(src):
            self._src.pop(src)
            return True
        return False

    def add_src(self, src: int, weight: float):
        """
        This function adds another node to be the source of this node.
        :param src: source node to connect.
        :param weight: the weight of the edge.
        :return:
        """
        if src != self._id:
            self._src[src] = weight

    def get_dest(self) -> dict:
        """
        :return: the dict of the destination nodes.
        """
        return self._dest

    def get_src(self) -> dict:
        """
           :return: the dict of the source nodes.
        """
        return self._src

    def get_weight(self, dest: int) -> float:
        """
        :param dest: given destination.
        :return: the weight of the edge this node it's the source of the given destination.

        """
        return self._dest.get(dest)

    def getKey(self) -> int:
        """
        :return: the key of the node.
        """
        return self._id

    def setKey(self, id: int):
        """
        set new key to the node.
        :param id: given key.
        """
        self._id = id

    def getPos(self) -> tuple:
        """
        :return:t 3 coordinates tuple .
        """
        return self._pos

    def setPos(self, pos: tuple):
        """
        set the position of the node.
        :param pos: tuple of the coordinates.
        """
        self._pos = pos

    def getWeight(self) -> float:
        """
        :return: the weight of the node.
        """
        return self._weight

    def setWeight(self, weight: float):
        """
        set new weight of the node.
        :param weight: the new weight.
        """
        self._weight = weight

    def getTag(self) -> int:
        """
        :return: the tag of the node.
        """
        return self._tag

    def setTag(self, tag: int):
        """
        set new tag to the node.
        :param tag: the new tag.
        """
        self._tag = tag

    def getInfo(self) -> str:
        """
        :return: the info associated with node.
        """
        return self._info

    def setInfo(self, info: str):
        """
        set new info to the node.
        :param info: string info .
        """
        self._info = info
