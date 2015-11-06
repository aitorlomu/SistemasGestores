def mcd(a,b):
    acop=a
    res=b
    resto=1
    while resto!=0:
        resto=acop%res
        acop=res
        if resto!=0:
            res=resto
    return res


print('se va a calcular el mcm')
a=int(input('Introduzca el número a '))
b=int(input('Introduzca el número b '))

print('El mcm de ',a,' y de ',b,'es ',(a*b)/mcd(a,b))
