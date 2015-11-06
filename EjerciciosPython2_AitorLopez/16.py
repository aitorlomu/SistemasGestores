def cambiarValores():    
    global realA
    global imaginariaA
    global realB
    global imaginariaB
    
    realA=int(input('introduzca el valor de la parte real del número complejo a '))
    imaginariaA=int(input('introduzca el valor de la parte imaginaria del número complejo  a '))
    realB=int(input('introduzca el valor de la parte real del número complejo b '))
    imaginariaB=int(input('introduzca el valor de la parte imaginaria del número complejo b '))

def sumar():
    global resReal
    global resImag
    resReal=realA+realB
    resImag=imaginariaA+imaginariaB
    print('El resultado es :',resReal,'+',resImag,'i')
    
def restar():
    resReal=realA-realB
    resImag=imaginariaA-imaginariaB
    print('El resultado es :',resReal,'+',resImag,'i')

def multiplicar():
    global res
    resReal=((realA*realB)-(imaginariaA*imaginariaB))
    resImag=((realA*imaginariaB)+(realB*imaginariaA))
    print('El resultado es :',resReal,'+',resImag,'i')

    
    
funcionar=1
leido =0
while(funcionar!=0):
    print('BIENVENIDO')
    print('1)Cambiar valores de los números complejos')
    print('2)sumar números')
    print('3)restar')
    print('4)multiplicar')
    print('5)dividir')
    print('0)Salir')
    funcionar=int(input('Seleccione una opción '))

    if funcionar==1:
        cambiarValores()
        leido=1
        
    if leido==1:
        if funcionar==2:
            sumar()
        if funcionar==3:
            restar()
        if funcionar==4:
            multiplicar()
                            
    else:
        print('Primero debe leer un los números complejos')
    
