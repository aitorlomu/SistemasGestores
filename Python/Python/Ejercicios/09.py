num=int(input('Introduzca el número de números que introducirá '))
max=0
for i in range(0,num):
    introducido=int(input('Introduce un número '))
    if introducido>max:
        max=introducido

print('El máximo valor es ',max)


