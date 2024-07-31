class Validation:

    @staticmethod
    def validate_non_empty_string(value: str, message: str):
        if not value or value.isspace():
            raise ValueError(message)

    @staticmethod
    def validation_positive_value(value, message: str):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def validate_table_number(table_number: int, min_number: int, max_number: int):
        if not (min_number <= table_number <= max_number):
            raise ValueError(f"Outside table's number must be between {min_number} and {max_number} inclusive!")


    @staticmethod
    def validate_if_exist(item: str, item_lst: list, message:str):
        if any(i.name == item for i in item_lst):
            raise ValueError(message)


    @staticmethod
    def table_duplivaty(number: int, tables: list, message:str):
        if any(t.table_number == number for t in tables):
            raise Exception(message)
