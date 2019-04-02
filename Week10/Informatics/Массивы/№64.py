N = int(input())
arr = input().split()
for y in range(N):
    if int(arr[y]) % 2 == 0:
        print(arr[y], end=' ')
