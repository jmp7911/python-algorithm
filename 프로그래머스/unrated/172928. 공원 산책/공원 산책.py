def solution(park, routes):
    answer = []
    W = len(park[0])
    H = len(park)
    #시작위치찾기
    a = [(i, x.index('S')) for i, x in enumerate(park) if 'S' in x]
    현위치 = a[0]
    #명령
    for y in routes:
        명령 = y.split(' ')
        방향 = 명령[0]
        거리 = int(명령[1])
        
        임시 = 현위치
        flag = True
        for _ in range(거리):
            if 방향 == 'E':
                임시 = (임시[0], 임시[1]+1)
            elif 방향 == 'W':
                임시 = (임시[0], 임시[1]-1)
            elif 방향 == 'S':
                임시 = (임시[0]+1, 임시[1])
            elif 방향 == 'N':
                임시 = (임시[0]-1, 임시[1])
            if 임시[0] >= H or 임시[1] >= W or 임시[0] < 0 or 임시[1] < 0:
                flag = False
                break
            else:
                try:
                    if park[임시[0]][임시[1]] == 'X':
                        flag = False
                        break
                except IndexError:
                    flag = False
                    break
                
        if flag:
            현위치 = 임시
        
        
    return 현위치