h=int(input('Introduzca las horas '))
m=int(input('Introduzca los minutos '))
s=int(input('Introduzca los segundos '))

h1=int(input('Introduzca las horas (2)'))
m1=int(input('Introduzca los minutos (2)'))
s1=int(input('Introduzca los segundos (2)'))

totalsegs=s+(m*60)+((h*60)*60)
totalsegs1=s1+(m1*60)+((h1*60)*60)

print('el primer tiempo es de ', totalsegs ,' segundos')
print('el segundo tiempo es de ', totalsegs1 ,' segundos')

print('La direrencia de segundos entre la primera y la segunda fecha es de '
      ,totalsegs-totalsegs1)
