class Validation:

    @staticmethod
    def valid_empty_str_or_white_space(word: str, message: str):
        if word == "" or word.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_age(age: int, min_age ,message: str):
        if min_age > age:
            raise ValueError(message)


    @staticmethod
    def valid_horse_name(name, message):
        if len(name) < 4:
            raise ValueError(mesage)

    @staticmethod
    def valid_horse_speed(speed, max_speed, message):
        if speed > max_speed:
            raise ValueError(message)
