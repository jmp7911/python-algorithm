def solution(name, yearning, photo):
    answer = []
    for x in photo:
        val = 0
        for y in x:
            try:
                val += yearning[name.index(y)]
            except ValueError:
                val += 0
        answer.append(val)
    return answer