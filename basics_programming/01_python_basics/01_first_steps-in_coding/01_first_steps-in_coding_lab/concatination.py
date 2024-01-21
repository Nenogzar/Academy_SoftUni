name=input("Моля запишете вашето име: ",)
print('Здравей ', end='') #
print(name)

print('Hello ' + name + '!')

firstname=input("Моля въведете вашето собствено име: ")
lastname=input("МОля въведете вашата фамилия: ")
age=int(input("На колко години сте?  "))
town=input("Къде живеете? ")
str=firstname + ' ' + lastname + ' @ ' + str(age)
print(str)

interp=(f"Вие сте {firstname} {lastname} на {age} години и живеете в {town}.")
print(interp)


