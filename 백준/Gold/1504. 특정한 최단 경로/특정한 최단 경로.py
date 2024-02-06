import sys
import heapq
INF = 2**64-1
answer = INF
N, E = map(int, sys.stdin.readline().split())
lines = [sys.stdin.readline().strip() for _ in range(E)]
v1, v2= map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for a in lines:
    i, j, c = map(int, a.split())
    graph[i].append((j, c))
    graph[j].append((i, c))

dist = [INF] * (N+1)
q = []
start = 1
dist[start] = 0
heapq.heappush(q, (0, start))

while q:
    cost, node = heapq.heappop(q)
    if dist[node] != cost:
        continue
    for d, c in graph[node]:
        if dist[d] > cost + c:
            dist[d] = cost + c
            heapq.heappush(q, (dist[d], d))


dist_v1 = [INF] * (N+1)
start = v1
dist_v1[start] = 0
heapq.heappush(q, (0, start))

while q:
    cost, node = heapq.heappop(q)
    if dist_v1[node] != cost:
        continue
    for d, c in graph[node]:
        if dist_v1[d] > cost + c:
            dist_v1[d] = cost + c
            heapq.heappush(q, (dist_v1[d], d))

dist_v2 = [INF] * (N+1)
start = v2
dist_v2[start] = 0
heapq.heappush(q, (0, start))

while q:
    cost, node = heapq.heappop(q)
    if dist_v2[node] != cost:
        continue
    for d, c in graph[node]:
        if dist_v2[d] > cost + c:
            dist_v2[d] = cost + c
            heapq.heappush(q, (dist_v2[d], d))
if dist[v1] == INF or dist[v2] == INF or dist[N] == INF:
    print(-1)
    sys.exit()
# 1 -> v1 -> v2 -> N
answer = min(answer, dist[v1] + dist_v1[v2] + dist_v2[N])
# 1 -> v2 -> v1 -> N
answer = min(answer, dist[v2] + dist_v2[v1] + dist_v1[N])
print(answer)