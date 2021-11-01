
import math
x=input ("Введите х: ")
q=input ("Введите q: ")
cos = 1
count = 1
zn = -1
x2 = x*x
f = 2 
n = 2
while ((x2/f) >= q ):
    cos = cos + zn*x2/f
    count = count + 1
    n = n + 2
    x2 = x2 * x * x
    f = f * (n - 1) * n
    zn = zn * (-1)
    print("cos(x): "+str(cos))

