from functools import reduce

def solution(n):
    temp_answer = [[0 for _ in range(1, i+2)] for i in range(n)]
    copy_n = n
    max_num = n*(n+1)//2
    counter = 1
    row, col = -1, 0
    direction = 'down' # 'down', 'right', 'up'
    while counter <= max_num:
        for _ in range(copy_n):
            if direction == 'down':
                row += 1
            elif direction == 'right':
                col += 1
            elif direction == 'up':
                row -= 1
                col -= 1
            temp_answer[row][col] += counter
            counter += 1
        else:
            copy_n -= 1
            if direction == 'down':
                direction = 'right'
            elif direction == 'right':
                direction = 'up'
            elif direction == 'up':
                direction = 'down'
    answer = reduce(lambda x,y : x + y, temp_answer)
    return answer