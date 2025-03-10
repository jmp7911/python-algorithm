N, K = map(int, input().split())

arr = []
for i in enumerate(range(N), 1):
    if N % i[0] == 0:
        arr.append(i[0])
if len(arr) < K:
    print(0)
else:
    print(arr[K-1])