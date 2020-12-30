class NodeData:
    def __init__(self, key: int, pos: tuple = None, weight: float = 0.0, tag: int = 0, info: str = "f"):
        self._key = key
        self._pos = pos
        self._weight = weight
        self._tag = tag
        self._info = info
        self._src = {}
        self._dest = {}

    def __repr__(self):
        return f"pos:{self._pos}"

    def add_dest(self, dest: int, weight: float):
        """
        This function adds another node to be the destination of this node.
        :param dest:
        :param weight:
        :return:
        """
        self._dest[dest] = weight

    def has_dest(self, dest: int) -> bool:
        for i in self._dest.keys():
            if i == dest:
                return True
        return False

    def has_src(self, src: int) -> bool:
        for i in self._src.keys():
            if i == src:
                return True
        return False

    def remove_dest(self, dest: int) -> bool:
        if self.has_dest(dest):
            self._dest.pop(dest)
            return True
        return False

    def remove_src(self, src: int) -> bool:
        if self.has_src(src):
            self._src.pop(src)
            return True
        return False

    def add_src(self, src: int, weight: float):
        """
        This function adds another node to be the source of this node.
        :param src:
        :param weight:
        :return:
        """
        self._src[src] = weight

    def get_dest(self) -> dict:
        return self._dest

    def get_src(self) -> dict:
        return self._src

    def get_weight(self, dest: int) -> float:
        return self._dest.get(dest)

    def getKey(self) -> int:
        return self._key

    def setKey(self, key: int):
        self._key = key

    def getPos(self) -> tuple:
        return self._pos

    def setPos(self, pos: tuple):
        self._pos = pos

    def getWeight(self) -> float:
        return self._weight

    def setWeight(self, weight: float):
        self._weight = weight

    def getTag(self) -> int:
        return self._tag

    def setTag(self, tag: int):
        self._tag = tag

    def getInfo(self) -> str:
        return self._info

    def setInfo(self, info: str):
        self._info = info
