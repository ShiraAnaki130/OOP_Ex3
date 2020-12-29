class EdgeData:
    def __init__(self, src: int = 0, dest: int = 0, weight: float = 0.0, tag: int = 0, info: str = "f"):
        self._src = src
        self._dest = dest
        self._weight = weight
        self._tag = tag
        self._info = info

    def getSrc(self) -> int:
        return self._src

    def setSrc(self, src: int):
        self._src = src

    def getDest(self) -> int:
        return self._dest

    def setDest(self, dest: int):
        self._dest = dest

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