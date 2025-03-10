X = []
Y = []
for _ in range(3):
    A,B=map(int, input().split())
    if A in X:
        X.remove(A)
    else:
        X.append(A)
    if B in Y:
        Y.remove(B)
    else:
        Y.append(B)
print(X[0], Y[0])