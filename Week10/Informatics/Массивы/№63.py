import scanf as scanf
N = int(input())
arr = input().split()
for i in range(N):
    if i % 2 == 0:
        print(int(arr[i]), end=' ')
