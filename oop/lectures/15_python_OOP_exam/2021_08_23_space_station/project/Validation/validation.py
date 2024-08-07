class Validate:

    @staticmethod
    def validation_empty_str_whitespace(name: str, message: str):
        if not name or name.isspace():
            raise ValueError(message)

    @staticmethod
    def space_station_astronaut_types(type_astronaut: str):
        if type_astronaut not in ("Biologist", "Geodesist", "Meteorologist"):
            raise Exception("Astronaut type is not valid!")
