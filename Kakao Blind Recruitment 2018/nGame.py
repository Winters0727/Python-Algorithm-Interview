def solution(n, t, m, p):
    def convert(number, n):
        if number == 0:
            return '0'

        n_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        n_stack = []
        n_num = number

        while n_num >= n:
            n_num, remain = divmod(n_num, n)
            n_stack.append(n_list[remain])
        
        if n_num:
            n_stack.append(n_list[n_num])
        
        result = ''.join(reversed(n_stack))
        return result
    
    num_str = ''
    number = -1
    limit = m*t
    while True:
        number += 1
        num_str += convert(number, n)
        if len(num_str) >= limit:
            break

    answer = ''
    for index in range(p-1, m*t, m):
        answer += num_str[index]
    return answer