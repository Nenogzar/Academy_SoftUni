class BaseDecoration:

    def __init__(self,comfort: int, price: float):
        self._comfort = comfort
        self._price = price

    @property
    def comfort(self):
        return self._comfort

    @property
    def price(self):
        return self._price

