from project.stores.base_store import BaseStore
from collections import defaultdict


class ToyStore(BaseStore):
    INITIAL_CAPACITY = 100

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        estimated_profit = self.get_estimated_profit()

        model_data = defaultdict(lambda: {'count': 0, 'total_price': 0.0})

        for product in self.products:
            model_data[product.model]['count'] += 1
            model_data[product.model]['total_price'] += product.price

        sorted_models = sorted(model_data.keys())

        toys_info = []
        for model in sorted_models:
            num_of_pieces = model_data[model]['count']
            avg_price = model_data[model]['total_price'] / num_of_pieces
            toys_info.append(f"{model}: {num_of_pieces}pcs, average price: {avg_price:.2f}")

        result = (
                f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                f"{estimated_profit}\n"
                "**Toys for sale:\n"
                + "\n".join(toys_info)
        )

        return result
