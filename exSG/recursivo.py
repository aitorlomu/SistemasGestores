def suma(n,i,cont):
    if(i==n):
        cont+=(-1**(i-1))*(1/(i**2))
        print(cont)
    else:
        cont+=(-1**(i-1))*(1/(i**2))
        i+=1
        suma(n,i,cont)
        
n=int(input('Introduzca un número '))
cont=0
suma(n,1,cont)

