def f():
    yield 5
    yield 3

a = f()
for n in list(range(1000000)):
    if n % 100000 == 0:
        print(n)


