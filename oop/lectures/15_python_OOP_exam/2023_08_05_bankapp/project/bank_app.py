from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []  # contain all loans (objects) that are created
        self.clients: List[BaseClient] = []  # contain all clients (objects) that are created

    @property
    def Valid_types_of_loans(self):
        return {"StudentLoan": StudentLoan,
                "MortgageLoan": MortgageLoan}

    @property
    def Valid_types_of_clients(self):
        return {"Student": Student,
                "Adult": Adult}

    @property
    def Valid_loat_to_person(self):
        return {"StudentLoan": Student,
                "MortgageLoan": Adult}

    def add_loan(self, loan_type: str):
        if loan_type not in self.Valid_types_of_loans:
            raise Exception("Invalid loan type!")

        new_loan = self.Valid_types_of_loans[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.Valid_types_of_clients:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return f"Not enough bank capacity."

        new_client = self.Valid_types_of_clients[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(c for c in self.clients if c.client_id == client_id)

        if not isinstance(client, self.Valid_loat_to_person[loan_type]):
            raise Exception("Inappropriate loan type!")

        loan = next(l for l in self.loans if type(l).__name__ == loan_type)
        self.loans.remove(loan)

        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next(c for c in self.clients if c.client_id == client_id)
        if not client:
            raise Exception("No such client!")
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = 0

        for loan in self.loans[:]:  # todo копие за да не се променя основния
            if isinstance(loan, self.Valid_types_of_loans[loan_type]):
                if loan not in [l for c in self.clients for l in c.loans]:
                    loan.increase_interest_rate()
                    changed_loans += 1

        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_clients += 1

        return f"Number of clients affected: {changed_clients}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)

        loans_count_granted_to_clients = sum(
            1 for client in self.clients for loan in client.loans
        )
        granted_sum = sum(loan.amount for client in self.clients for loan in client.loans)

        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum(loan.amount for loan in self.loans)

        avg_client_interest_rate = (
            sum(client.interest for client in self.clients) / total_clients_count
            if total_clients_count > 0
            else 0.0
        )

        stats = (
            f"Active Clients: {total_clients_count}\n"
            f"Total Income: {total_clients_income:.2f}\n"
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
            f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        )

        return stats
