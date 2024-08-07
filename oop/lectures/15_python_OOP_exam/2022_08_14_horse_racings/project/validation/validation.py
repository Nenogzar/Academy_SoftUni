from typing import List


class Validation:

    @staticmethod
    def valid_empty_str_or_white_space(word: str, message: str):
        if word == "" or word.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_age(age: int, min_age: int, message: str):
        if age < min_age:
            raise ValueError(message)

    @staticmethod
    def valid_horse_name(name: str, message: str):
        if len(name) < 4:
            raise ValueError(message)

    @staticmethod
    def valid_horse_speed(speed: int, max_speed: int):
        if speed > max_speed:
            raise ValueError("Horse speed is too high!")

    @staticmethod
    def adjust_horse_speed(current_speed: int, increase: int, max_speed: int) -> int:
        if current_speed + increase > max_speed:
            return max_speed
        return current_speed + increase

    @staticmethod
    def valid_type(type_type: str, valid_types: List[str], message: str):
        if type_type not in valid_types:
            raise ValueError(message)
