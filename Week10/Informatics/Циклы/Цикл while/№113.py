import math
N = int(input())
i=1
while i <= N:
    if math.sqrt(i) % 1 == 0:
        print(i)
    i += 1

