from collections import Counter

def solution(s):
    counter, zero_counter = 0, 0
    while s != '1':
        counter += 1
        num_counter = Counter(s)
        zero_counter += num_counter['0']
        s = bin(num_counter['1'])[2:]
        
    answer = [counter, zero_counter]
    return answer