length = int(input())
width = int(input())
height = int(input())
parcent = float(input())

capacity = length * width * height
capacity_l = capacity/1000
parcent_balast = 1-(parcent/100)
wather_l = capacity_l * parcent_balast
print(wather_l)
