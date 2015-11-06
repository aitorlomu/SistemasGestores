def calcFactorialImpar(num):
    cont=1
    for i in range(1,num+1):
        if(i%2)!=0:
            cont=cont*i
    print('El factorial impar de ',num,' es ',cont)

num=int(input('Introducir el número del que se calculará el factorial '))
calcFactorialImpar(num)


