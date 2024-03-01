input_products = input().split(" ")
products = {}

for n in range(0, len(input_products), 2):
    # key, value = input_products[n], input_products[n + 1]
    # products[key] = int(value)
    products = {input_products[i]: int(input_products[i + 1]) for i in range(0, len(input_products), 2)}


def check_products(product_dict):
    results = []
    for product in product_dict:
        if product not in products:
            results.append(f"Sorry, we don't have {product}")
        else:
            results.append(f"We have {products[product]} of {product} left")
    return results


new_check = input().split(" ")
check_results = check_products(new_check)
for result in check_results:
    print(result)
