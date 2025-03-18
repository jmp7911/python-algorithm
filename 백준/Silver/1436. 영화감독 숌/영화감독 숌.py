N = int(input())

i = 0
while True:
    i += 1
    if str(i).find('666') != -1:
        N -= 1
        if N == 0:
            print(i)
            break