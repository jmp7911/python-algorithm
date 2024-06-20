def solution(users, emoticons):
    from itertools import product
    
    # 할인율 리스트
    discount_rates = [10, 20, 30, 40]
    
    # 가능한 모든 할인율 조합 생성
    all_combinations = list(product(discount_rates, repeat=len(emoticons)))
    
    best_subscribers = 0
    best_revenue = 0
    
    for combination in all_combinations:
        subscribers = 0
        revenue = 0
        
        for user in users:
            user_rate, user_limit = user
            total_cost = 0
            
            for i in range(len(emoticons)):
                if combination[i] >= user_rate:
                    total_cost += emoticons[i] * (100 - combination[i]) // 100
            
            if total_cost >= user_limit:
                subscribers += 1
            else:
                revenue += total_cost
        
        if subscribers > best_subscribers or (subscribers == best_subscribers and revenue > best_revenue):
            best_subscribers = subscribers
            best_revenue = revenue
    
    return [best_subscribers, best_revenue]
