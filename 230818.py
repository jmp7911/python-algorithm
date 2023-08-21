def solution(data):
    flag1 = answer = 0
    for i, chr in enumerate(data):
        if flag1 == 1:
            if chr == '1':
                flag1 = 2
            else:
                answer += int(chr) if chr.isnumeric() else 0
                flag1 = 0
        elif flag1 == 2:
            flag1 = 0
            if chr == '0':
                answer += 10
            else:
                answer += 1
        else:
            if chr in ['r','e','v']:
                flag1 = 1
    
    if flag1 == 2:
        answer += 1
    answer = str(answer)
    return answer[0]+'월'+answer[1] + '일'