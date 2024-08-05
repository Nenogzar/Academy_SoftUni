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
    def valid_stanima(stanima, min_stamina, max_stamina, message):
        # if stanima not in range(min_stamina, max_stamina+1):
        if stanima < min_stamina and stanima > max_stamina:
            raise ValueError(message)
