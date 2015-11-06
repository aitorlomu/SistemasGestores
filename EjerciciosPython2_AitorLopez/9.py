def compruebaAmigos(x,y):
    a=sumaDivisores(x)
    b=sumaDivisores(y)
    if a==y and b==x:
        return True
    else:
        return False





def sumaDivisores(x):
    suma=0

    for i in range (1,int(x/2)+1):
        if(x%i)==0:
            suma+=i
    print(suma)
    return suma


a=int(input('introduzca el número a para saber si es amigo '))
b=int(input('introduzca el número b para saber si es amigo '))

if compruebaAmigos(a,b):
    print('Los números son amigos')
else:
    print('Los números no son amigos')


