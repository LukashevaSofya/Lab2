
#import math
 
#def my_sin (x,n):
 
 
    #x = x/180*math.pi
    #x = x%(360)
 
    #q = x
    #s = 0
 
   # for i in range(1, n+1):
       # s = s+ q
       # q = q* (-1) * (x*x) / ((2*i+1) * (2*i))
 
 
    #return s
 
 
#print(my_sin(float(input("enter x")),int(input("enter n"))))
from math import cos, factorial, radians
x = radians(float(input("Enter the angle value: ")))
q = int(input("Enter a number: "))
n=2
#n = int(input("Enter a number: "))
cosinus = sum(
    #pow(-1, i) * pow(x, 2 * i) / factorial(2 * i) for i in range(n))
    pow(-1, i) * pow(x, 2 * i) / factorial(2 * i) for i in range(n))
while cosinus< q:
    
    print("cosinus:\t%s" % cosinus)
print("math.cos:\t%s" % cos(x))
