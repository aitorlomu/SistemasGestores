import re

cadena =  input("Escribe lo que quieras ")
cadena = re.sub("\D", "", cadena)

print(cadena)
