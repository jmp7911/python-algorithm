import itertools
import sys
N, M = map(int, sys.stdin.readline().split())

for i in itertools.permutations(range(1, N+1), M):
    print(' '.join(map(str, i)))