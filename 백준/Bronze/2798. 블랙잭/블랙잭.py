from itertools import combinations
N,M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for x in combinations(arr,3):
    if sum(x) <= M:
        answer = max(answer, sum(x))
        if sum(x) == M:
            break
print(answer)

