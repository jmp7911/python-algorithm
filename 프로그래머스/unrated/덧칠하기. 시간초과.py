def solution(n, m, section):
    arr = list()
    #i번 벽부터 칠할 때 칠해지는 벽의 최댓값
    for i in range(1, n-m+2):
        max_ = len(list(filter(lambda x: x in range(i,i+m) , section)))
        arr.append(max_)
    
    wall = len(section)
    i = 0
    while wall > 0:
        cnt = max(arr)
        wall -= cnt
        del arr[arr.index(cnt):m]
        i += 1
        
    
    return i
