def formBhaskara(a,b,c):
    delta = (b**2) - 4 * a * c

    if delta < 0:
        print("Impossivel calcular")
        exit()
    elif a == 0:
        print("Impossivel calcular")
        exit()
    
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)

a, b, c = map(float, input().split())
formBhaskara(a, b, c)