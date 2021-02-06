from collections import Counter

def solution(words):
    answer = 0
    char_list = list(''.join(words))
    char_counter = Counter(char_list)
    for word in words:
        length = len(word)
        for index in range(length):
            if char_counter[index] == 1:
                answer += index
                break
        else:
            answer += length
        print(answer)
    return answer