num=int(input('Introducir el número del que se calculará el factorial '))
cont=1
for i in range(1,num+1):
    cont=cont*i
print('El factorial de ',num,' es ',cont)
