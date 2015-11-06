num=input('Introduzca un número para comprobar si es capicua ')
invertido=''

for i in range(len(num)-1,-1,-1):
    invertido=invertido + num[i]

if num==invertido:
    print('Es capicua')
else:
    print('No es capicua')
