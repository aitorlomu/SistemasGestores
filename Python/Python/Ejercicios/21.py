contletras=int(input('Introduzca el número de caracteres que se introducirá '))
char=input('Introduzca la letra a contabilizar ')
contchar=0;


for i in range(0,contletras):
    let=input('Introduzca una letra ')
    if let==char:
        contchar=contchar+1

print('La letra ',char,' ha aparecido ',contchar,' veces')
