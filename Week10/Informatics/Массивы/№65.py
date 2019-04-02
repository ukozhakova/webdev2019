N = int(input())
arr = input().split()
cnt = 0

for x in range(N):
    if int(arr[x]) > 0:
        cnt += 1
print(cnt)
