a=int(input('escriba el número a '))
b=int(input('escriba el número b '))
acop=a
res=b
resto=1
while resto!=0:
    resto=acop%res
    acop=res
    if resto!=0:
        res=resto
        
print('El mcd de ',a,' y de ',b,' es ',res)
