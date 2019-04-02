import math
N = int(input())
i = 0
while N > 1:
    if N % 2 == 0:
        N /= 2
    else:
        break
if N > 1:
    print('NO')
else:
    print('YES')

