number_juniors = int(input())   # броят младши велосипедисти. Цяло число в интервала [1…100]
number_seniors = int(input())   # броят старши велосипедисти. Цяло число в интервала [1… 100]
type_trace = input()            # вид трасе – "trail", "cross-country", "downhill" или "road"

taxe_rate_juniors = 0
tax_rate_seniors = 0
number_cyclists = number_seniors + number_juniors
if type_trace == "trail":
    taxe_rate_juniors = 5.5
    tax_rate_seniors = 7
elif type_trace == "cross-country":
    taxe_rate_juniors = 8
    tax_rate_seniors = 9.5
    #print(taxe_rate_juniors)
    #print(tax_rate_seniors)
    if number_cyclists >= 50:
        taxe_rate_juniors *= 0.75
        tax_rate_seniors *= 0.75
        #print(taxe_rate_juniors)
        #print(tax_rate_seniors)
elif type_trace == "downhill":
    taxe_rate_juniors = 12.25
    tax_rate_seniors = 13.75
elif type_trace == "road":
    taxe_rate_juniors = 20
    tax_rate_seniors = 21.5


all_taxes = number_seniors * tax_rate_seniors + number_juniors * taxe_rate_juniors
#print(f"all_taxes: {all_taxes}")

amount_donated = all_taxes - (all_taxes * 0.05)

print(f"{amount_donated:.2f}")


# cyclists_juniors = int(input())
# cyclists_seniors = int(input())
# route_type = input()
#
# tournament_info = {
#     "juniors": {
#         "trail": 5.50,
#         "cross-country": 8,
#         "downhill": 12.25,
#         "road": 20,
#         "tax": 0.05,
#         "off": 0.25},
#     "seniors": {
#         "trail": 7,
#         "cross-country": 9.50,
#         "downhill": 13.75,
#         "road": 21.50}
#
# }
# total_cyclists = cyclists_juniors + cyclists_seniors
#
# if route_type == "cross-country" and total_cyclists >= 50:
#     junior_total = (tournament_info["juniors"][route_type] - (tournament_info["juniors"][route_type]) \
#                    * tournament_info["juniors"]["off"]) * cyclists_juniors
#     seniors_total = (tournament_info["seniors"][route_type] - (tournament_info["seniors"][route_type]) \
#                     * tournament_info["juniors"]["off"]) * cyclists_seniors
#     total = junior_total + seniors_total
#     total += - (total * tournament_info["juniors"]["tax"])
# else:
#     junior_total = tournament_info["juniors"][route_type] * cyclists_juniors
#     seniors_total = tournament_info["seniors"][route_type] * cyclists_seniors
#     total = junior_total + seniors_total
#     total += - (total * tournament_info["juniors"]["tax"])
#
# print(f"{total:.2f}")