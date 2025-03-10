T = int(input())
N = [int(input()) for _ in range(T)]
coins = [25, 10, 5, 1]
for i in N:
    answer = []
    for coin in coins:
        answer.append(i // coin)
        i %= coin
    print(" ".join(map(str, answer)))