def validate_non_empty_string(value: str, message: str):
    if not value or not value.strip():
        raise ValueError(message)


def validation_positive_value(value, message: str):
    if value <= 0:
        raise ValueError(message)


def validate_table_number(table_number: int, min_number: int, max_number: int, message: str):
    if not (min_number <= table_number <= max_number):
        raise ValueError(message)
