class GeoLocation:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self._x = x
        self._y = y
        self._z = z

    def getX(self) -> float:
        return self._x

    def getY(self) -> float:
        return self._y

    def getZ(self) -> float:
        return self._z

    def distance(self, pos) -> float:
        if type(pos) == GeoLocation:
            dis_x=(self._x - pos.getX()) ** 2
            dis_y=(self._y - pos.getY()) ** 2
            dis_z=(self._z - pos.getZ()) ** 2



