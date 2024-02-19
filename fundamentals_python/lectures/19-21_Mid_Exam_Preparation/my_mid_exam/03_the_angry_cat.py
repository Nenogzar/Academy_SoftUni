def cheap_summing(side, entry_point):
    return sum([x for x in side if x < entry_point])

def expensive_summing(side, entry_point):
    return sum([x for x in side if x >= entry_point])

def main():
    price_rating = [int(x) for x in input().split(", ")]
    entry_point = int(input())
    type_of_items = input()

    left_side = price_rating[:entry_point]
    right_side = price_rating[entry_point + 1:]
    entry_point_value = price_rating[entry_point]

    if type_of_items == "cheap":
        if cheap_summing(left_side, entry_point_value) >= cheap_summing(right_side, entry_point_value):
            print(f"Left - {cheap_summing(left_side, entry_point_value)}")
        else:
            print(f"Right - {cheap_summing(right_side, entry_point_value)}")
    elif type_of_items == "expensive":
        if expensive_summing(left_side, entry_point_value) >= expensive_summing(right_side, entry_point_value):
            print(f"Left - {expensive_summing(left_side, entry_point_value)}")
        else:
            print(f"Right - {expensive_summing(right_side, entry_point_value)}")

if __name__ == "__main__":
    main()


"""" """

def calculate_low_cost(aList, points):
    cost = 0
    for item in aList:
        if item < points:
            cost += item
    return cost

def calculate_high_cost(aList, points):
    cost = 0
    for item in aList:
        if item >= points:
            cost += item
    return cost

def main():
    priceRatings = list(map(int, input().split(", ")))
    entryPoint = int(input())
    targetType = input()
    costTarget = priceRatings[entryPoint]
    rightList = priceRatings[entryPoint + 1:]
    leftList = priceRatings[:entryPoint]
    if targetType == "cheap":
        leftDamage = calculate_low_cost(leftList, costTarget)
        rightDamage = calculate_low_cost(rightList, costTarget)
    elif targetType == "expensive":
        leftDamage = calculate_high_cost(leftList, costTarget)
        rightDamage = calculate_high_cost(rightList, costTarget)
    if leftDamage >= rightDamage:
        print(f"Left - {leftDamage}")
    else:
        print(f"Right - {rightDamage}")

if __name__ == "__main__":
    main()