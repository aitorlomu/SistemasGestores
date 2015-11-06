def calcularFactorial(num):
    suma=1
    for i in range(1,num+1):
        suma=suma*i
    return suma

def calcularCombinatorio(m,n):
    return calcularFactorial(m)/(calcularFactorial(n)*calcularFactorial(m-n))

print('Se va a calcular el número combinatorio de 2 números')
m=int(input('Introduzca el número m '))
n=int(input('Introduzca el número n '))

res=calcularCombinatorio(m,n)

print('El resultado combinatorio de ',m,' y ', n,' es ',res)

