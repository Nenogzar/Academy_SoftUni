class Validation:

    @staticmethod
    def valid_not_empty_not_white_space(value, message):
        if value =="" or value.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_number(value, validation, message):
        if value <= validation:
            raise ValueError(message)




