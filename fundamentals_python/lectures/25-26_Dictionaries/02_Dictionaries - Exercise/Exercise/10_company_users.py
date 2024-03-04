"""  dictionary whit value[list]"""

companies_info = input()
dict_compani = {}

while companies_info != "End":
    compani, reg_num = companies_info.split(" -> ")

    if compani not in dict_compani:
        dict_compani[compani] = [reg_num]
    else:
        if reg_num not in dict_compani[compani]:
            dict_compani[compani].append(reg_num)

    companies_info = input()

for compani, register_list in dict_compani.items():
    print(compani)
#     for reg_number in register_list:
#         print(f"-- {reg_number}")
    [print(f"-- {reg_num}") for reg_num in register_list]



"""Kumchovalcho """
company_info = {}

company_employee = input()
while company_employee != "End":
    company_employee = company_employee.split(" -> ")
    company, employee = company_employee[0], company_employee[1]

    company_info[company] = company_info.get(company, [])
    if employee not in company_info[company]:
        company_info[company].append(employee)

    company_employee = input()

for key in company_info:
    print(key)
    [print(f"-- {employee}") for employee in company_info[key]]
#
#
#
#
""" CEO - whit Function and whit value{dictionary} """

command = input()

company_info = {}


def employee_id_search(id):
    for value in company_info[id].values():
        if id == value:
            return True
    return False


while command != "End":
    company_name, employee_id = command.split(" -> ")
    company_info[company_name] = company_info.get(company_name, {})
    if not employee_id_search(company_name):
        company_info[company_name][employee_id] = employee_id
    command = input()

for name_uni in company_info:
    print(name_uni)
    for key, value in company_info[name_uni].items():
        print(f"-- {value}")

""" Ivan Shopov  whit sorted dictionary"""

companies = {}
command = input().split(" -> ")
while command[0] != "End":
    company = command[0]
    id = command[1]
    if company in companies.keys():
        if id not in companies[company]:
            companies[company].append(id)
    else:
        companies[company] = []
        companies[company].append(id)
    command = input().split(" -> ")
companies = dict(sorted(companies.items(), key=lambda x: (x[0])))
for value in companies.values():
    value = sorted(value, key=lambda x: (value))
for key in companies.keys():
    print(f"{key}")
    for value in companies[key]:
        print(f"-- {value}")
