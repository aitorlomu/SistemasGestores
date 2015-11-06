num=float(input('Introduzca un número'))
suma=num;
cont=1;
while num>0:
    num=float(input('Introduzca un número'))
    suma=suma+num;
    cont+=1
media=suma/cont
print('Se han introducido ',cont,' números y su media es de ',media)
