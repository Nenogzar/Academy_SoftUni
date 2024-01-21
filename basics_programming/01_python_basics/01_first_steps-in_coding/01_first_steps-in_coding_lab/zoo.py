dog=int(input("Брой на кучета: "))
animals=int(input("Брой на други животни: "))
dogprice = dog * 2.5
animalsprice= animals * 4

razhod= dogprice + animalsprice
rezultat=(f"Разход за зареждане на храна за {dog} кучета и {animals} други животни е: {razhod} лв.")
print(rezultat)

