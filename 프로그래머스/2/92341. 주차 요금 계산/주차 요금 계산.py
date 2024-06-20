import math
def solution(fees, records):
    answer = []
    #1 records로 부터 차량번호별 주차시간
    results_IN = dict()
    results = dict()
    for x in records:
        t, car_id, flag = x.split(" ")
        HH, MM = list(map(int, t.split(":")))
        
        if flag == "IN":
            results_IN[car_id] = HH * 60 + MM
            
        elif flag == "OUT":
            results[car_id] = results.get(car_id, 0) + (HH * 60 + MM) - results_IN[car_id]
            results_IN.pop(car_id)
        
    #2 입차기록만 있는 차량 주차시간
    for car_id, minutes in results_IN.items():
        results[car_id] = results.get(car_id, 0) + (1439 - results_IN[car_id])
    #3 차량번호별 주차요금 계산
    for car_id, sum_minutes in sorted(results.items()):
        print(car_id, sum_minutes)
        if sum_minutes <= fees[0]:
            answer.append(fees[1])
        else:
            
            answer.append(fees[1] + math.ceil((sum_minutes - fees[0]) / fees[2]) * fees[3])
    
    return answer