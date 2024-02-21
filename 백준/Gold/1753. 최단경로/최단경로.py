import sys
import heapq

INF = 2**64-1
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
lines = [sys.stdin.readline() for _ in range(E)]
graph = [[] for _ in range(V+1)]

for a in lines:
    u, v, w = map(int, a.split())
    graph[u].append((v, w))

dist = [INF] * (V+1)
q = []
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

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
    