N = int(input())
arr = input().split()
isTrue = False

for y in range(N-1):
    if int(arr[y]) * int(arr[y+1]) > 0:
        isTrue = True
        break
if isTrue:
    print("YES")
else:
    print("NO")
