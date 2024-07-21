class BaseEntity:
    id= 1

    @classmethod
    def get_next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id
