num=input('Introduce un número para calcular el producto de sus cifras ')
total=1
if num[0]=='-':
    for i in range(1,len(num)):
        total=total*(-1*(int(i)))
    print(total)
else:
    for i in num:
        total=total*int(i)
    print(total)
