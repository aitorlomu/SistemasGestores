def compruebaVocal(n):
    if n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='A' or n=='E' or n=='I' or n=='O' or n=='U':
        return True
    else:
        return False

    
espacio=False
letra=input('Introduzca una letra ')
suma=0
while letra!=' ':
    if compruebaVocal(letra):
        print('Es vocal')
        suma+=1
    else:
        print('No es vocal')

    letra=input('Introduzca una letra ')

print('El número de vocales es de ',suma)




