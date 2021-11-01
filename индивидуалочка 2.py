a = int(input("Введите а: "))
b = int(input("Введите b: "))
if a<b:
  print("a должно быть больше b")
i=0
s = 0
for i in range(a, b+1):
  if i % 2 == 1:
    s =+ i    
    print(s)
