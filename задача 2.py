
import math

n = int(input("Введите количество слогаемых: "))

p = 0

for i in range(1, n+1, 2):
    p += 4 / i - 4 / (i+2)

print("Приблизительное значение pi : " + str(p))




    
