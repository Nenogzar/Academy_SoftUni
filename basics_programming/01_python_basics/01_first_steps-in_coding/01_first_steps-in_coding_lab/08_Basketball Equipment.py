annual_fee = int(input())

sneakers = annual_fee * 0.60
team = sneakers * 0.80
ball = team * 0.25
accessory = ball / 5

total_price = annual_fee + sneakers + team + ball + accessory
print(total_price)