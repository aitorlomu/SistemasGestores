anio=int(input('Introduzca un año '))

if(anio%4)==0:
    if(anio%100)==0:
        if(anio%400)==0:
            print('el año ',anio,' es bisiesto')
        else:
            print('el año ',anio,' no es bisiesto')
    else:
        print('el año ',anio,' es bisiesto')

