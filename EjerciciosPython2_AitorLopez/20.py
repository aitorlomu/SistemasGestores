original = [['a', 'b'], ['c', 'd'], ['e','f']]
transpuesta = [[' ',' ',' '],[' ',' ',' ']]
 
for i in range(0,3):
    for j in range(0,2):
        transpuesta[j][i] = original[i][j]

for i in range(3):
    print(original[i])
for i in range(2):
    print(transpuesta[i])
   




