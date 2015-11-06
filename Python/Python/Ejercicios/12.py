num=int(input('Introduce un número para saber si es primo '))
contador=0
for i in range(1,int((num/2)+1)):
    if(num%i)==0:
        contador=contador+1
    if contador>2:
        print('El número ',num,' no es primo')
        break

if contador<=2:
    print('El número ',num,' es primo')
    
