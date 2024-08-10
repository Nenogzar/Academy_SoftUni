from project.bank_app import BankApp
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan

try:
    lm = MortgageLoan()
    print(lm.amount)
    print(lm.interest_rate)
    lm.increase_interest_rate()
    print(lm.interest_rate)
    print("***************")
    ls = StudentLoan()
    print(ls.amount)
    print(ls.interest_rate)
    ls.increase_interest_rate()
    print(ls.interest_rate)


except Exception as e:
    print(e)


bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))

print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
