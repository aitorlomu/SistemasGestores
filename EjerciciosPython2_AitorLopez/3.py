def comprobarPrimo(num):  
    contador=0
    for i in range(1,int(num+1)):
        if(num%i)==0:
            contador=contador+1
        if contador>2:
            #print('El número ',num,' no es primo')
            return False
    if contador<=2:
        print(num) 
        return True

num1=int(input('Introduce un número inicial del recorrido '))
num2=int(input('Introduce un número final '))
cont=0
for i in range(num1,num2+1):
    if comprobarPrimo(i):
        cont+=1

if cont==0:
    print('No hay números primos')
