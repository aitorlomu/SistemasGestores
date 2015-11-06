num=int(input('Introduzca un número para comprobar si es perfecto '))
if num>=0:
    r=num
    suma=0
    while r>0:
        if (num%r)==0:
            suma=suma+(num/r)
        r=r-1
    if (suma-num)==num:
        print('El número es perfecto')
    else:
        print('El número no es perfecto')

    
else:
    print('El número es negativo')
