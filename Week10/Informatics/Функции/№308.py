def f(a, b):
    if float(a) != float(b):
        return 1
    else:
        return 0


m, n = input().split()
print(f(m, n))
