numeros=int(input('Introduzca el número de números que se desea introducir '))
suma=0;
cont=1;
num=0;
for i in range (0,numeros):
    num=int(input('Introduzca un número'))
    suma=suma+num;

media=suma/numeros
print('Se han introducido ',numeros,' números y su media es de ',media)
