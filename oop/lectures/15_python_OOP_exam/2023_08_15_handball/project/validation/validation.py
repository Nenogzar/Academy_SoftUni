class Validate:

    @staticmethod
    def empty_str_white_space(value, message):
        if value == '' or value.isspace:
            return message

    @staticmethod
    def less_than(value, message):
        if len(value) < 2:
            return message

    @staticmethod
    def less_than_equal(value, less, message):
        if value <= less:
            return message