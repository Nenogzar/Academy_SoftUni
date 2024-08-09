class Validation:

    @staticmethod
    def validate_empty_str_white_space(value, message):
        if value =="" or value.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_number(value, valid_number, message):
        if value <= valid_number:
            raise ValueError(message)

    @staticmethod
    def valid_positive_number(value,message):
        if value < 0:
            raise ValueError(message)
