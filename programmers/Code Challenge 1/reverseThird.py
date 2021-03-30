# def solution(n):
#     temp_answer = []
#     def to_third(num):
#         nonlocal temp_answer
#         num, mod = divmod(num, 3)
#         temp_answer.append(mod)
#         if num >= 3:
#             to_third(num)
#         else:
#             temp_answer.append(num)
#     to_third(n)
#     temp_answer = ''.join(map(str,temp_answer))
#     answer = int(temp_answer, 3)
#     return answer

def solution(n):
    if n < 3:
        return n
        
    answer = 0
    temp_num = []
    def to_third(num):
        nonlocal temp_num
        num, mod = divmod(num, 3)
        temp_num.append(mod)
        if num >= 3:
            to_third(num)
        else:
            temp_num.append(num)
    to_third(n)
    num_count = 1
    while temp_num:
        answer += num_count * temp_num.pop()
        num_count *= 3
    return answer