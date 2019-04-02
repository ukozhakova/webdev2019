import math
x = int(input())
cnt = 0
for m in range(1, 1 + int(math.sqrt(x))):
    if x % m == 0:
        cnt = cnt+1
if math.sqrt(x) % 1 == 0:
    print(cnt*2-1)
else:
    print(cnt*2)


