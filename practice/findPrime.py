from itertools import permutations
import math

def solution(numbers):
    answer = 0
    new_numbers = []
    length = len(numbers)
    for n in range(1, length+1):
        permutation = list(permutations(numbers,n)) 
        for case in permutation:
            number = int(''.join(case))
            if number not in new_numbers:
                new_numbers.append(number)
    max_num = max(new_numbers)
    checker = [True for _ in range(max_num+1)]
    checker[0], checker[1] = False, False
    for num in range(2, round(math.sqrt(max_num))+1):
        for n in range(num*2, max_num+1, num):
            checker[n] = False
    for num in new_numbers:
        if checker[num]:
            answer += 1
    return answer