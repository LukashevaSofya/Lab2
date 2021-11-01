import cmath
import math
import sys
a=float(input("Введите а: "))
while a==0:
    print("а не может равняться нулю")
    sys.exit()
b=float(input("Введите b: "))
c=float(input("Введите c: "))
discr = b ** 2 - 4 * a * c
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    x1=(-b+cmath.sqrt(discr))/2*a
    x2=(-b-cmath.sqrt(discr))/2*a
    print(x1)
    print(x2)
