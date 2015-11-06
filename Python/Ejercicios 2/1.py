a=float(input('Introduce el valor de a '))
b=float(input('Introduce el valor de b '))
c=float(input('Introduce el valor de c '))
d=float(input('Introduce el valor de d '))
e=float(input('Introduce el valor de e '))
f=float(input('Introduce el valor de f '))

comp = a * e - b * d
 
if comp != 0 :
    x = (e * c - b * f) / comp
    y = (a * f - d * c) / comp
 
    print('La solucion al sistema es x= %d e y= %d' % (x, y))
 
else :
    m = d / a
 
    if m * c == f :
        print('El sistema tiene infinitas soluciones')
    else:
        print('El sistema no tiene soluciones')
