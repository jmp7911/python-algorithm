N = int(input())
sosu = []
for i in range(2, 1001):
    flag = True
    for j in enumerate(range(i // 2 + 1), 2):
        if i != j[0] and i % j[0] == 0:
            flag = False
            break
    if flag:
        sosu.append(i)
A = list(map(int,input().split()))
count = sum(1 for x in A if x in sosu)
print(count)