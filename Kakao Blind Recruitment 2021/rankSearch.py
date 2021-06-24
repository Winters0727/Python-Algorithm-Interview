from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    answer = []
    recruit_dict = defaultdict(list)
    combination = []
    for k in range(5):
        combination += list(combinations(range(4),k))
    for recruit in info:
        *skills, point = recruit.split(' ')
        point = int(point)
        for comb in combination:
            key_string = ''
            for i in range(4):
                if i in comb:
                    key_string += '-'
                else:
                    key_string += skills[i]
            recruit_dict[key_string].append(point)
    
    for key in recruit_dict.keys():
        recruit_dict[key].sort()
    
    for q in query:
        counter = 0
        *skills, food_and_point = q.split(' and ')
        food, point = food_and_point.split(' ')
        skills += [food]
        point = int(point)
        key_string = ''.join(skills)
        answer.append(len(recruit_dict[key_string]) - bisect.bisect_left(recruit_dict[key_string], point))
    return answer