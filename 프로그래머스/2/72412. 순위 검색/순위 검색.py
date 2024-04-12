def solution(info, query):
    answer = []
    
    
    
    # table["java"]["backend"]["junior"]["pizza"] = [150]
    # table[0][0][0][0] = [150]
    # print(table)
    idx = [["cpp", "java", "python", "-"], ["backend", "frontend", "-"], ["junior", "senior", "-"], ["pizza", "chicken", "-"]]
    
    lang, pos, pro, food = idx
    
    table = dict()
    
    for a in lang:
        for b in pos:
            for c in pro:
                for d in food:
                    table.setdefault((a, b, c, d), list())
    
    for i in info:
        ii = i.split()
        
        for a in [ii[0], "-"]:
            for b in [ii[1], "-"]:
                for c in [ii[2], "-"]:
                    for d in [ii[3], "-"]:
                        table[(a, b, c, d)].append(int(ii[4]))
    # print(table)
    for j in table:
        table[j].sort()
    
    for q in query:
        qq = q.split()
        
        a, b, c, d = [qq[0], qq[2], qq[4], qq[6]]
        
        pool = table[(a, b, c, d)]
        
        stand = int(qq[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= stand:
                r = mid
            else:
                l = mid+1
        
        answer.append(len(pool)-l)
    return answer