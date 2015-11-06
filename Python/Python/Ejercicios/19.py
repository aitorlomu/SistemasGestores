x=int(input('Introduzca el número x '))
y=int(input('Introduzca el número y '))

aux=x;
res=0;

while aux>0:
    res+=1
    aux=aux-y

print(res)
