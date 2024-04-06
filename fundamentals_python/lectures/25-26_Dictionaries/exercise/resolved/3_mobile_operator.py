contract_term = input()
contract_type = input()
mobile_internet = input()
mounts_to_pay = int(input())

tax_to_pay = 0
discount_two_year_contract = 1

if contract_term == "one":
    if contract_type == "Small":
        tax_to_pay = 9.98

    elif contract_type == "Middle":
        tax_to_pay = 18.99

    elif contract_type == "Large":
        tax_to_pay = 25.98

    elif contract_type == "ExtraLarge":
        tax_to_pay = 35.99

elif contract_term == "two":
    if contract_type == "Small":
        tax_to_pay = 8.58

    elif contract_type == "Middle":
        tax_to_pay = 17.09

    elif contract_type == "Large":
        tax_to_pay = 23.59

    elif contract_type == "ExtraLarge":
        tax_to_pay = 31.79


if mobile_internet == "yes":
    if tax_to_pay <= 10:
        tax_to_pay += 5.50

    elif tax_to_pay <= 30:
        tax_to_pay += 4.35

    elif tax_to_pay > 30:
        tax_to_pay += 3.85

total_price_to_pay = tax_to_pay * mounts_to_pay

if contract_term == "two":
    discount_two_year_contract = 0.9625

total_price_to_pay = (tax_to_pay * mounts_to_pay) * discount_two_year_contract

print(f"{total_price_to_pay:.2f} lv.")


""" Dictionary"""

contract_term = input()
contract_type = input()
mobile_internet = input()
months_to_pay = int(input())

tax_to_pay = 0
discount_two_year_contract = 1

tax_rates = {
    "one": {
        "Small": 9.98,
        "Middle": 18.99,
        "Large": 25.98,
        "ExtraLarge": 35.99
    },
    "two": {
        "Small": 8.58,
        "Middle": 17.09,
        "Large": 23.59,
        "ExtraLarge": 31.79
    }
}

tax_to_pay = tax_rates[contract_term][contract_type]

internet_dict = {"tax_to_pay":[
                        {"margin":10,"addition": 5.50},
                        {"margin":30,"addition": 4.35},
                        ]

                }
if mobile_internet == "yes":
    for condition in internet_dict["tax_to_pay"]:

        if tax_to_pay <= condition["margin"]:
            tax_to_pay += condition["addition"]
            break
    else:
        tax_to_pay += 3.85

total_price_to_pay = tax_to_pay * months_to_pay

if contract_term == "two":
    discount_two_year_contract = 0.9625

total_price_to_pay *= discount_two_year_contract  # Correct way to apply the discount

print(f"{total_price_to_pay:.2f} lv.")





