import math
v = int(input())
t = int(input())
if v*t > 109:
    print((v*t) % 109)
elif v*t < 109:
    print(int(109-math.fabs(v*t)) % 109)
