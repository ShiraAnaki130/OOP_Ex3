from src.GeoLocation import GeoLocation


class NodeData:
    def __init__(self, pos: GeoLocation, key: int, weight: float = 0.0, tag: int = 0, info: str = "f"):
        self._pos = pos
        self._key = key
        self._weight = weight
        self._tag = tag
        self._info = info
        self._src = {}
        self._dest = {}

    def addDest(self, dest: int, weight: float):
        """
        This function adds another node to be the destination of this node.
        :param dest:
        :param weight:
        :return:
        """
        self._dest[dest] = weight

    def addSrc(self, src: int, weight: float):
        """
        This function adds another node to be the source of this node.
        :param src:
        :param weight:
        :return:
        """
        self._dest[src] = weight

    def getDest(self) -> dict:
        return self._dest

    def getSrc(self) -> dict:
        return self._src

    def getKey(self) -> int:
        return self._key

    def setKey(self, key: int):
        self._key = key

    def getPos(self) -> GeoLocation:
        return self._pos

    def setPos(self, pos: GeoLocation):
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
