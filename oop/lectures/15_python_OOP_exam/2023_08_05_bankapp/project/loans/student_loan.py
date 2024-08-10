from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    rate_base = 1.5
    amount_base = 2000

    def __init__(self):
        super().__init__(self.rate_base, self.amount_base)
        self.increase_rate = 0.2
    def increase_interest_rate(self):
        self.interest_rate += self.increase_rate
