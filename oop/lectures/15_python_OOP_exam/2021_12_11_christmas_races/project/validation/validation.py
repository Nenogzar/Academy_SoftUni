class Validation:
    @staticmethod
    def valid_model(model: str, message: str):
        if len(model) < 4:
            raise ValueError(message)

    @staticmethod
    def valid_speed(valid_speed: int, min_speed: int, max_speed: int, message: str):
        if valid_speed not in range(min_speed, max_speed + 1):
            raise ValueError(message)

    @staticmethod
    def valid_driver_name(name: str, message: str):
        if not name or name.isspace():
            raise ValueError(message)

