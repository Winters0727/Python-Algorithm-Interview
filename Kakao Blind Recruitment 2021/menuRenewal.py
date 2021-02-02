from collections import defaultdict, Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    food_counter = defaultdict(list)
    for index, foods in enumerate(orders):
        for food in foods:
            food_counter[food].append(index+1)
    for c in course:
        food_comb = []
        for key in food_counter.keys():
            if len(food_counter[key]) >= c:
                food_comb += list(combinations(food_counter[key], c))
        if food_comb:
            answer_counter = Counter(food_comb)
            print(max(answer_counter.most_common(), key=lambda x : x[1]))
    return answer