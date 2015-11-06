def deBinAInt(n):
    suma=0
    for i in range(n-1,-1,-1):
        num=int(input(('Introduzca el bit correspondiente a la posición (sólo 0 o 1 o petará el programa) ',i,' ')))
        suma=suma+(num*(2**i))
    return suma
def deBinAIntdecc(n):
    suma=0
    for i in range(-1,(n*-1)-1,-1):
        num=int(input(('Introduzca el bit correspondiente a la posición (sólo 0 o 1 o petará el programa) ',i,' ')))
        suma=suma+(num*(2**i))
    return suma


nentera=int(input('Introduzca los bits que tendrá la parte entera '))
nfraccional=int(input('Introduzca los bits que tendrá la parte fraccional '))

print(deBinAInt(nentera)+deBinAIntdecc(nfraccional))
