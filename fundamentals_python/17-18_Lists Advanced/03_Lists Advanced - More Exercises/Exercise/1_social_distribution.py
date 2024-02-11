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