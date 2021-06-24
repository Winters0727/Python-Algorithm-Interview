def solution(rows, columns, queries):
    def turn_table(table, query):
        copy_table = [table[r][:] for r in range(rows)]
        top, left, bottom, right = query
        top -= 1
        left -= 1
        bottom -= 1
        right -= 1
        
        min_value = float('INF')
        row, col = top, left
        prev_val = copy_table[top][left]
        direction = 'right'
        
        while True:
            if prev_val < min_value:
                min_value = prev_val
            
            if (row, col) == (top, left) and direction == 'up':
                break

            if direction == 'right':
                col += 1
                prev_val, copy_table[row][col] = copy_table[row][col], prev_val
                if col == right:
                    direction = 'down'

            elif direction == 'down':
                row += 1
                prev_val, copy_table[row][col] = copy_table[row][col], prev_val
                if row == bottom:
                    direction = 'left'

            elif direction == 'left':
                col -= 1
                prev_val, copy_table[row][col] = copy_table[row][col], prev_val
                if col == left:
                    direction = 'up'

            elif direction == 'up':
                row -= 1
                prev_val, copy_table[row][col] = copy_table[row][col], prev_val

        return copy_table, min_value

    answer = []

    table = [[row*columns+col+1 for col in range(columns)] for row in range(rows)]
    
    for query in queries:
        table, min_value = turn_table(table, query)
        answer.append(min_value)

    return answer