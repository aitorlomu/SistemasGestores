def explicar_programa():
    print('Este es un programa que calculará el valor de la intensdad que pasa a través de una resistencia')

def obtener_valores():
    global v
    v=float(input('Introduzca el voltaje en Voltios '))
    global r
    r=float(input('Introduzca la resistencia en ohmios '))
    

def calcular():
    global i
    i=v/r
    

def imprimir_respuesta():
    print('Un voltaje de ',v,' y una resistencia de ',r,' da ',i,' Amperios')



explicar_programa()
obtener_valores()
calcular()
imprimir_respuesta()
