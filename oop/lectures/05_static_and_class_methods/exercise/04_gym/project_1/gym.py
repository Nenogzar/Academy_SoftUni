from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer

class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = next(
            (sub for sub in self.subscriptions if sub.id == subscription_id),
            None
        )

        if not subscription:
            return f"Subscription with ID {subscription_id} not found."

        customer = next(
            (cust for cust in self.customers if cust.id == subscription.customer_id),
            None
        )
        trainer = next(
            (tr for tr in self.trainers if tr.id == subscription.trainer_id),
            None
        )
        equipment = next(
            (eq for eq in self.equipment if eq.id == subscription.exercise_id),
            None
        )
        plan = next(
            (pl for pl in self.plans if pl.id == subscription.exercise_id),
            None
        )

        info = []
        info.append(subscription.__repr__())
        info.append(customer.__repr__() if customer else "Customer not found")
        info.append(trainer.__repr__() if trainer else "Trainer not found")
        info.append(equipment.__repr__() if equipment else "Equipment not found")
        info.append(plan.__repr__() if plan else "Plan not found")

        return "\n".join(info)
