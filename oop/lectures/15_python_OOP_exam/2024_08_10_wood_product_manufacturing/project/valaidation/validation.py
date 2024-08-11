class Validation:
    @staticmethod
    def validate_len_white_space(value, length, message):
        if len(value.strip()) < length :
            raise ValueError(message)

    @staticmethod
    def validate_les_or_equal(value, les, message):
        if value <= les:
            raise ValueError(message)


    @staticmethod
    def valid_empty_white_space(value,message):
        if value == "" or value.isspace():
            raise ValueError(message)


    @staticmethod
    def three_white_space(value, message):
        if len(value) != 3 or " " in value:
            raise ValueError(message)

    @staticmethod
    def validate_positive_number(value, message):
        if value < 0:
            raise ValueError(message)
