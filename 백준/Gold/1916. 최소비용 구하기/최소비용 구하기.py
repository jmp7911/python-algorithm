import sys
import heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [sys.stdin.readline().strip() for _ in range(M)]
start, end = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for b in bus:
    i, j, c = map(int, b.split())
    graph[i].append((j, c))

costs = [2**64-1] * (N+1)
q = []

heapq.heappush(q, (0, start))

while q:
    cost, node = heapq.heappop(q)
    if costs[end] < cost:
        continue
    for d, c in graph[node]:
        if costs[d] > cost + c:
            costs[d] = cost + c
            heapq.heappush(q, (costs[d], d))

print(costs[end])
