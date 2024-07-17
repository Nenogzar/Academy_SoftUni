class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget  # private
        self.__animal_capacity = animal_capacity  # private
        self.__workers_capacity = workers_capacity  # private

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if price > self.__budget:
            return "Not enough budget"

        if self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for pos, x in enumerate(self.workers):
            if x.name == worker_name:
                del self.workers[pos]
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary = sum(x.salary for x in self.workers)
        if workers_salary <= self.__budget:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tended_animals = sum(x.money_for_care for x in self.animals)
        if tended_animals <= self.__budget:
            self.__budget -= tended_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += int(amount)

    def _generate_status(self, entities):
        info = {entity.__class__.__name__: [] for entity in entities}
        for entity in entities:
            info[entity.__class__.__name__].append(str(entity))
        return info

    def _format_status(self, info, entity_name):
        output = [f"You have {sum(len(v) for v in info.values())} {entity_name}"]
        entity_order = ["Lion", "Tiger", "Cheetah"] if entity_name == "animals" else ["Keeper", "Caretaker", "Vet"]
        for entity_class in entity_order:
            if entity_class in info:
                output.append(f"----- {len(info[entity_class])} {entity_class}s:")
                output.extend(info[entity_class])
        return "\n".join(output)

    def animals_status(self):
        info = self._generate_status(self.animals)
        return self._format_status(info, "animals")

    def workers_status(self):
        info = self._generate_status(self.workers)
        return self._format_status(info, "workers")
