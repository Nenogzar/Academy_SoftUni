l=int(input("каква е дължината? "))
w=int(input("каква е ширината? "))
h=int(input("каква е височината? "))
procent=(int(input("какъв процент от акварума е зает? ")))
aquaruim=l*w*h
aqua_l=aquaruim*0.001
aqua_pers=procent*0.01
total_l=aqua_l*(1-aqua_pers)
print(total_l)