import itertools
def solution(numbers, target):
    answer = 0
    maximun = sum(numbers)
    for i in range(1, len(numbers)+1):
        answer += [maximun - sum(x) * 2 for x in itertools.combinations(numbers, i)].count(target)
        
    return answer