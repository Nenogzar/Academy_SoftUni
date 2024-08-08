class Validation:

    @staticmethod
    def valid_str_or_white_space(value, valid_number, message):
        if len(value) < valid_number or value.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_number(age, valid_age, message):
        if age < valid_age:
            raise ValueError(message)

    @staticmethod
    def validate_ganre_or_music(value: str, valid_list: [], message: str):
        if value not in valid_list:
            raise ValueError(message)
