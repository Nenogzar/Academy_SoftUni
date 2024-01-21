kvadrat = float(input("Въведете квадратурата на обекта: "))
price = kvadrat * 7.61
discount = (price * 18)/100
endprce = price - discount

ofer=(f"Стандартна цена на офертата е {price}лв. прилагаме 18% отстъпка, равностойна на{discount}, и формираме крайна цена {endprce}лв.")
print(ofer)