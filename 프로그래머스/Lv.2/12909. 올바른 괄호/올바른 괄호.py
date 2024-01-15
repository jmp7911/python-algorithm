def solution(s):
    answer = True
    
    stack = []
    # '(' =>  push ')' => pop
    for x in s:
        if x == '(':
            stack.append('(')
        elif x == ')':
            if not stack:
                return False
            else:
                stack.pop()
        
    return True if not stack else False
    
