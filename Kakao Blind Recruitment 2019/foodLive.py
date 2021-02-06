import heapq

def solution(food_times, k):
    length = len(food_times)
    
    if sum(food_times) <= k:
        return -1
    elif k < length:
        return k+1
    elif k == length:
        return 1
    
    foods = []
    check_index = [False for _ in range(length)]
    for index, food in enumerate(food_times):
        heapq.heappush(foods, (food, index))
    
    count_k = k
    eat_length = length
    eat_count = 0
    while True:
        food, index = heapq.heappop(foods)
        if food <= eat_count:
            check_index[index] = True
            continue
        circle, remain = divmod(count_k, eat_length-eat_count)
        if circle < food - eat_count:
            break
        else:
            check_index[index] = True
            count_k = (circle-food+eat_count)*(eat_length-eat_count) + remain
            eat_count = food
    
    find_answer = False
    while not find_answer:
        for index in range(length):
            if check_index[index]:
                continue
            else:
                if remain == 0:
                    answer = index+1
                    find_answer = True
                    break
                else:
                    remain -= 1

    if answer > length:
        answer -= length
    return answer