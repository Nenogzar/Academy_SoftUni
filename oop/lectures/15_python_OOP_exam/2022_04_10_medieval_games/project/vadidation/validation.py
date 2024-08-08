class Validation:

    @staticmethod
    def valid_name(name: str, message: str):
        if len(name) == 0:
            raise ValueError(message)

    @staticmethod
    def valid_positive_energi(energi: int, message: str):
        if energi < 0:
            raise ValueError(message)

    @staticmethod
    def valid_unic_name(name: str, list_name: list, message: str):
        if name in list_name:
            raise Exception(message)

    @staticmethod
    def valid_age(age: int, message: str):
        if age < 12:
            raise ValueError(message)

    @staticmethod
    def valid_stanima(stamina, min_stamina, max_stamina, message):
        if not min_stamina <= stamina <= max_stamina:
        # if stamina not in range(min_stamina, max_stamina+1):
            raise ValueError(message)
