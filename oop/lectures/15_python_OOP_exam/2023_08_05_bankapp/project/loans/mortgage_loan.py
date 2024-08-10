from project.loans.base_loan import BaseLoan


class MortgageLoan (BaseLoan):
    rate_base = 3.5
    amount_base = 50000.00

    def __init__(self):
        super().__init__(self.rate_base, self.amount_base)
        self.increase_rate = 0.5

    def increase_interest_rate(self):
        self.interest_rate += self.increase_rate


