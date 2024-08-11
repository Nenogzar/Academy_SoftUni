class Validation:

    @staticmethod
    def valid_white_space_empty_string(string:str, message:str):
        if len(string) == 0 and string.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_price(price: float, message:str):
        if price <= 0:
            raise ValueError(message)