""" 1 """

wealth_numbers = list(map(int, input().split(", ")))
minimum_wealth = int(input())

for i in range(len(wealth_numbers)):
    wealthiest = wealth_numbers.index(max(wealth_numbers))

    number = wealth_numbers[i]
    if number < minimum_wealth:
        wealth_difference = minimum_wealth - number
        wealth_numbers[i] += wealth_difference

        wealth_numbers[wealthiest] -= wealth_difference
        if wealth_numbers[wealthiest] < minimum_wealth:
            print('No equal distribution possible')
            break

else:
    print(wealth_numbers)


""" 2 """


wealth = list(map(int, input().split(", ")))
min_wealth = int(input())

if min_wealth > sum(wealth) / len(wealth):
    print("No equal distribution possible")
    exit()
else:
    for i in range(len(wealth)):
        num = wealth[i]
        if num < min_wealth:
            result = min_wealth - num
            max_waelt = max(wealth)
            index_max_num = wealth.index(max_waelt)
            check_num = max_waelt - result
            wealth[i] = min_wealth
            wealth[index_max_num] = check_num

print(wealth)