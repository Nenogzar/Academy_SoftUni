from project.software.software import Software


class Aditional:

    @staticmethod
    def enough_capacity(capacity: int,
                       total_memory: int,
                       software_object: list,
                       software: object,
                       message: str):
        if sum(s.capacity_consumption for s in software_object) + software.capacity_consumption > capacity or sum(
                s.memory_consumption for s in software_object) + software.memory_consumption > total_memory:
            raise Exception(message)

    @staticmethod
    def hardware_exist(hardware_name: str, hardware_list: list, message: str):
        for h in hardware_list:
            if h.name == hardware_name:
                return h
        return message


    @staticmethod
    def search_exist(item_name: str, item_list: list):
        for it in item_list:
            if it.name == item_name:
                return it

        return "No item"
