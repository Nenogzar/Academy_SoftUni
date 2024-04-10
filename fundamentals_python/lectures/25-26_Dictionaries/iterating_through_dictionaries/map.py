fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

def apply_discount(product, discount=0.05):
    return product[0], round(product[1] * (1 - discount), 2)

map1 = dict(map(apply_discount, fruits.items()))
print(map1)
    # {'apple': 0.38, 'orange': 0.33, 'banana': 0.24}
map2 = dict(map(lambda item: apply_discount(item, 0.1), fruits.items()))
print(map2)
    # {'apple': 0.36, 'orange': 0.32, 'banana': 0.23}
map3 = dict(map(lambda item: apply_discount(item, 0.15), fruits.items()))
print(map3)
    # {'apple': 0.34, 'orange': 0.3, 'banana': 0.21}
