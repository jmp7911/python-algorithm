while True:
    try:
        N = int(input())
        if N == -1:
            break
        arr = []
        for i in enumerate(range(N//2 + 1), 1):
            if N % i[0] == 0:
                arr.append(i[0])
        if sum(arr) == N:
            print(f'{N} =', " + ".join(map(str,arr)))
        else:
            print(f'{N} is NOT perfect.')
    except:
        break