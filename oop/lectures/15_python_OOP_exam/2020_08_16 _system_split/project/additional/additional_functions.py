class Additional:

    @staticmethod
    def enough_capacity(capacity: int, total_memory: int, software_objects: list, software: object, message: str):
        if sum(s.capacity_consumption for s in software_objects) + software.capacity_consumption > capacity or \
                sum(s.memory_consumption for s in software_objects) + software.memory_consumption > total_memory:

            raise Exception(message)
