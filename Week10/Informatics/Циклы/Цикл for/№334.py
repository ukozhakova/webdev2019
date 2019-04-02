a = int(input())
b = int(input())
c = int(input())
d = int(input())
for r in range(a, b+1):
    if r%d == c:
        print(r, end=' ')
