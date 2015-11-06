encontrado=False
suma=0
n=12
while encontrado==False:
    suma=0
    lim=int(n/2)
    for i in range(1,lim):
        if((n%i)==0):
            suma+=i
           
        
    if(suma>n):
        encontrado=True
        print ('El primer número abundante es ',n)
    else:
        print (n,' no es')
        n+=1


