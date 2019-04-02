import math
N = int(input())
i = 0
while math.pow(2,i) <= N:
        print(int(math.pow(2, i)), end=' ')
        i += 1

