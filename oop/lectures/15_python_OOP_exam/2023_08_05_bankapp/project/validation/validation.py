class Validation:

    @staticmethod
    def vaid_empty_white_space(value, message):
        if value == ""  or value.isspace():
            raise  ValueError(message)


    @staticmethod
    def valid_10_symbols(value, message):
        if len(value) != 10:
            raise ValueError(message)


    @staticmethod
    def value_positiv_number(value, message):
        if value <= 0:
            raise ValueError(message)
