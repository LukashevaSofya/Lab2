
d=int(input("Введите день: "))
m=int(input("Введите месяц: "))
y=int(input("Введите год: "))
if m>12:
    input("Месяцев всего 12")
if (m== 4 or 6 or 9 or 11) and (d>30):
    input("В этом месяце всего 30 дней")
if m==2 and y%4==0 and d>29 :
    input("В этом месяце всего 29 дней")
    
if (m==2)and d>28:
    input("В этом месяце всего 28 дней")
if (m== 1 or 3 or 5 or 7 or 8 or 10 or 12) and (d>31):
    input("В этом месяце максимум 31 день")
if d<10:
    d= "0"+str(d)
if m<10:
    m= "0"+str(m)
if y<10:
    y="000"+str(y)
elif y<100:
    y="00"+str(y)
elif y<1000:
    y="0"+str(y)
elif y <2021:
    input("ммммм будущее")
input(str(d)+"."+str(m)+"."+str(y)+".")
