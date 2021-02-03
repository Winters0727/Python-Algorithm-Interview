from collections import defaultdict, Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for case in course:
        food_counter = defaultdict(int)
        for order in orders:
            if len(order) < case:
                continue
            else:
                comb_list = list(combinations(list(order),case))
                for comb in comb_list:
                    food_counter[''.join(sorted(comb))] += 1
        if food_counter.values():
            max_val = max(food_counter.values())
            if max_val >= 2:
                for key in food_counter.keys():
                    if food_counter[key] == max_val:
                        answer.append(key)
    answer.sort()
    return answer