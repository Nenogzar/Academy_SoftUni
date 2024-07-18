from typing import List, Union

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity <= len(self.animals):
            return f"Not enough space for animal"
        if self.__budget < price:
            return f"Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(w.salary for w in self.workers)
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_price = sum(p.money_for_care for p in self.animals)
        if self.__budget < total_price:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_price
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount:int):
        self.__budget += amount

    def get_status(self, items: List[Union[Animal, Worker]], item_types: List[str]) -> str:
        counts = {item_type: [] for item_type in item_types}
        for item in items:
            class_name = item.__class__.__name__
            if class_name in counts:
                counts[class_name].append(repr(item))

        result = [f"You have {len(items)} {items[0].__class__.__name__.lower()}s"] if items else [f"You have 0 {items[0].__class__.__name__.lower()}s"]
        for item_type in item_types:
            result.append(f"----- {len(counts[item_type])} {item_type}s:")
            result.extend(counts[item_type])

        return '\n'.join(result)

    def animals_status(self) -> str:
        return self.get_status(self.animals, ["Lion", "Tiger", "Cheetah"])

    def workers_status(self) -> str:
        return self.get_status(self.workers, ["Keeper", "Caretaker", "Vet"])
