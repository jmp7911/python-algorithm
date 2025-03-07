N,M = map(int,input().split())
answer = [[0] * M for _ in range(N)]
for i in range(N):
    answer[i] = list(map(int,input().split()))
for i in range(N):
    answer[i] = list(map(lambda a,b: a + b, answer[i], list(map(int,input().split()))))

for i in range(N):
    print(*answer[i])