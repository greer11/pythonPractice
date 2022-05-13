def fibo():
    a,b = 0,1
    x = 0
    while True:
        yield a
        a,b = b, b + a
        x += 1

for i in fibo():
    print(i)
