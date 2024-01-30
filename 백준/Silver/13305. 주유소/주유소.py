import sys
input=sys.stdin.readline

def solution():
    N = int(input())
    distance = list(map(int, input().split()))
    gas = list(map(int, input().split()))

    gas_min = gas.pop(0)
    price = 0
    for i in range(N-1):
        price += gas_min * distance[i]
        gas_min = min(gas_min, gas[i])
    
    return price

print(solution())