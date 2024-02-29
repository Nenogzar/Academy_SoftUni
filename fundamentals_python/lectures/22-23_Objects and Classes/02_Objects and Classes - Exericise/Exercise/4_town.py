class Town:
    def __init__ (self, name: str):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"


    def set_latitude(self, latitude: str) -> None:
        self.latitude = latitude

    def set_longitude(self, longitude: str) -> None:
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)