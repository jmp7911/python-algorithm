M = int(input())
N = int(input())
sosu = []
for i in range(2, 10001):
    flag = True
    for j in enumerate(range(i // 2 + 1), 2):
        if i != j[0] and i % j[0] == 0:
            flag = False
            break
    if flag:
        sosu.append(i)
arr = [x for x in sosu if x >= M and x <= N]
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))