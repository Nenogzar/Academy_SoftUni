airline = input()
ticket_for_adults = int(input())
ticket_for_children = int(input())
price_for_adults = float(input())
price_for_children = price_for_adults * 0.3
price_of_service_charge = float(input())
all_tickets = ticket_for_adults + ticket_for_children

total_price_adults = price_for_adults * ticket_for_adults
total_price_children = price_for_children * ticket_for_children
total_service_charge = all_tickets * price_of_service_charge

total_sum = total_price_adults + total_price_children + total_service_charge

profit_for_the_agency = total_sum * 0.2

print(f"The profit of your agency from {airline} tickets is {profit_for_the_agency:.2f} lv.")
