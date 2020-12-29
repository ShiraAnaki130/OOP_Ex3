class GeoLocationInterface:
    def get_x(self) -> float:
        pass

    def get_y(self) -> float:
        pass

    def get_z(self) -> float:
        pass

    def distance(self, pos: GeoLocation = None) -> float:
        pass