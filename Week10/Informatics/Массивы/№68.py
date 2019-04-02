N = int(input())
arr = input().split()
cnt = 0

for y in range(1, N-1):
    if int(arr[y]) > int(arr[y-1]) and int(arr[y]) > int(arr[y+1]):
        cnt += 1
print(cnt)
