while True:
    try:
        a = []
        a = list(map(int, input().split()))
        a.sort()
        if a[0] == 0 and a[1] == 0 and a[2] == 0:
            break
        if a[0] + a[1] <= a[2]:
            print("Invalid")
        elif len(set(a)) == 1:
            print("Equilateral")
        elif len(set(a)) == 2:
            print("Isosceles")
        elif len(set(a)) == 3:
            print("Scalene")
    except:
        break
