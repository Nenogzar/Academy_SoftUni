class Validation:

    @staticmethod
    def valid_white_space_empty_string(string:str, message:str):
        if len(string) == 0 or string.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_price(price: float, message:str):
        if price <= 0:
            raise ValueError(message)

    @staticmethod
    def positiv_number(number, message):
        if number < 0:
            raise ValueError(message)

    @staticmethod
    def validate_type(value, valivation_dict: dict,message):
        if value not in valivation_dict:
            raise Exception(message)


