n=int(input('Introduzca un número '))

suma=0

for i in range(1,n+1):
    suma+=(-1**(i-1))*(1/(i**2))


print("La solución es: ",suma)
