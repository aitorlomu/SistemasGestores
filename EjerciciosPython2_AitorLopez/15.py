def imprimir(a,b,c):
    
    print(a,'x**2 +',b,'x+',c)

def leer():    
    global a
    global b
    global c
    a=int(input('introduzca el valor de a '))
    b=int(input('introduzca el valor de b '))
    c=int(input('introduzca el valor de c '))

funcionar=1
leido =0
while(funcionar!=0):
    print('BIENVENIDO')
    print('1)Leer un polinomio de 2º grado')
    print('2)Imprimir polinomio de 2º grado')
    print('0)Salir')
    funcionar=int(input('Seleccione una opción '))

    if funcionar==1:
        leer()
        leido=1
    if funcionar==2:
        if leido==1:
            imprimir(a,b,c)
        else:
            print('Primero debe leer un polinomio')
    
