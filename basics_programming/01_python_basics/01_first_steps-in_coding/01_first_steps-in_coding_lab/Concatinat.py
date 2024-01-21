FirstName = input('Въведете вашето малко име:', )
LastName= input('Сега Фамилното име:', )
Age=input('На каква възразст сте?', )
Str= FirstName +' '+ LastName +' '+'& '+ str(Age) +' години'
print(Str)

x = int(input('Въведете стойност на X'))
y = int(input('Въведете стойност на Y'))
sum1 = 'Долепването на X до Y е '+ str(x)+str(y)   # concatination
sum = 'Сумата на X+Y=',x+y                # sum
print((sum1),'->sum1')
print((sum),'->sum')