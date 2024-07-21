# base_entity.py
class BaseEntity:
    _id = 1

    @classmethod
    def _generate_id(cls):
        id = cls._id
        cls._id += 1
        return id

    @classmethod
    def get_next_id(cls):
        return cls._id
