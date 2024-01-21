price_berry=float(input("Каква е цената на ягодите? "))
kg_babanas=float(input("Колко килограма банани са нужни? "))
kg_portokal=float(input("Колко килограма портокали са нужни? "))
kg_malini=float(input("Колко килограма малини са нужни? "))
kg_berry=float(input("Колко килограма ягоди са нужни? "))

price_malini=price_berry/2
price_portokal=price_malini - price_malini*0.4
price_bababas=price_malini - price_malini*0.8

total=price_berry*kg_berry+price_bababas*kg_babanas+price_portokal*kg_portokal+price_malini*kg_malini
print(total)