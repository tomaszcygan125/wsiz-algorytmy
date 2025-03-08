import math
def oblicz_rownanie_kwadratowe(a,b,c):
    if a == 0:
        print('to nie jest rownanie kwadratowe')
    else:
        d = (b**2) - (4 * a * c)
        print('d = ' , d)
        if d > 0:
            x1 = (-b - math.sqrt(d)) / 2*a
            x2 = (-b + math.sqrt(d)) / 2*a
            return x1, x2
        elif d == 0:
            x0 = -b / 2*a
            return x0
        elif d < 0:
            print('brak rozwiazan')

a = -6
b = 5
c = 2


print(oblicz_rownanie_kwadratowe(a,b,c))