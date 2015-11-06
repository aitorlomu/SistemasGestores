def factorial(num):
    cont=1
    for i in range(1,num+1):
        cont=cont*i
    return cont

ter=int(input('Introduzca el número de términos que desea '))
e=1

for i in range(1,ter):
    e=e+(1/factorial(i))

print('El número e es ',e)
