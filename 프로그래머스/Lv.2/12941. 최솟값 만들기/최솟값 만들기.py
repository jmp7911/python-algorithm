def solution(A,B):
    answer = 0

    # 최대의 값과 최소의 값을 곱하여 결과값이 최소값을 기대
    A_ = sorted(A, reverse=True)
    B_ = sorted(B)
    
    
    answer = sum([a * b for a, b in zip(A_, B_)])

    return answer