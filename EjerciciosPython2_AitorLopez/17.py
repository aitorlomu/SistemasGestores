dinero = float(input("Cuánto dinero tiene: "))
 
formato = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5,0.2,0.1,0.05,0.02,0.01]

for i in formato:
    if i<=8:
        
        print("%d monedas de %d" % ((dinero / i), i))
        dinero = dinero % i
    else:
        print("%d billetes de %d" % ((dinero / i), i))
        dinero = dinero % i

