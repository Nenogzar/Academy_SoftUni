from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name  # name of the factory.
        self.income = 0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    @property
    def product_typs(self):
        return {'Chair': Chair,
                'HobbyHorse': HobbyHorse}

    @property
    def store_typs(self):
        return {"FurnitureStore": FurnitureStore,
                "ToyStore": ToyStore}

    def produce_item(self, product_type: str, model: str, price: float) -> str:
        if product_type not in self.product_typs:
            raise Exception("Invalid product type!")

        product_class = self.product_typs[product_type]
        product = product_class(model, price)
        self.products.append(product)

        return f"A product of sub-type {product_class.SUB_TYPE} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.store_typs:
            raise Exception(f"{store_type} is an invalid type of store!")

        store_class = self.store_typs[store_type]
        store = store_class(name, location)
        self.stores.append(store)

        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct) -> str:
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        matching_products = []
        for product in products:
            if store.store_type == "FurnitureStore" and product.get_sub_type() == "Furniture":
                matching_products.append(product)
            elif store.store_type == "ToyStore" and product.get_sub_type() == "Toys":
                matching_products.append(product)

        if not matching_products:
            return "Products do not match in type. Nothing sold."

        for product in matching_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price

        return f"Store {store.name} successfully purchased {len(matching_products)} items."

    def unregister_store(self, store_name: str):
        store = next((store for store in self.stores if store.name == store_name), None)

        if store is None:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str) -> str:
        products_to_discount = [p for p in self.products if p.model == product_model]
        products_count = len(products_to_discount)

        for product in products_to_discount:
            if isinstance(product, HobbyHorse):
                product.discount()  # Отстъпка от 20%
            elif isinstance(product, Chair):
                product.discount()  # Отстъпка от 10%

        return f"Discount applied to {products_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        product_models = {}
        for product in self.products:
            if product.model not in product_models:
                product_models[product.model] = 0
            product_models[product.model] += 1

        sorted_product_models = sorted(product_models.items())

        store_names = sorted(store.name for store in self.stores)
        total_stores_count = len(self.stores)

        formatted_income = f"{self.income:.2f}"
        products_count = len(self.products)
        products_sum_price = sum(product.price for product in self.products)
        formatted_products_sum_price = f"{products_sum_price:.2f}"

        result = []
        result.append(f"Factory: {self.name}")
        result.append(f"Income: {formatted_income}")
        result.append("***Products Statistics***")
        result.append(f"Unsold Products: {products_count}. Total net price: {formatted_products_sum_price}")

        for model, count in sorted_product_models:
            result.append(f"{model}: {count}")

        result.append(f"***Partner Stores: {total_stores_count}***")
        result.extend(store_names)

        return "\n".join(result)
