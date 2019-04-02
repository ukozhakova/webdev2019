import math
a = int(input())
b = int(input())
for m in range(a, b+1):
    if math.sqrt(m)%1==0:
        print(m, end=' ')
