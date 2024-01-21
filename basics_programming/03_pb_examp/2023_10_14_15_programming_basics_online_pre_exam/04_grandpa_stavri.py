days_number = int(input())
total_jack = 0
total_degree = 0

for day in range(days_number):
    quantity_jack = float(input())                  # количество ракия
    degree_jack = float(input())                    # градуси на ракията
    total_jack += quantity_jack                     # цялото количество
    total_degree += degree_jack * quantity_jack
average_degrees_jack = total_degree / total_jack    # градуси на общата смес

print(f"Liter: {total_jack:.2f}")
print(f"Degrees: {average_degrees_jack:.2f}")

if 38 > average_degrees_jack:
    print("Not good, you should baking!")
elif 42 > average_degrees_jack:
    print("Super!")
else:
    print("Dilution with distilled water!")
