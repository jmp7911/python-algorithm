def solution(s):
    answer = []
    
    acc, count_zero = func1(s)
    return [acc, count_zero]

def func1(s, acc=0, count_zero=0):
    if len(s) == 1:
        return (acc, count_zero)
    
    ch = s.maketrans('','','0')
    s_ = s.translate(ch)
    
    return func1(format(len(s_), 'b'), acc+1, count_zero+ len(s) - len(s_))
    
    
    