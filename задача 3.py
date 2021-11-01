
fib1=1
fib2=1
while (fib2 < 10000):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum

    if (fib2 >= 1000):
        f=str(fib2)
        print(len(f)," Элемента")
        break


