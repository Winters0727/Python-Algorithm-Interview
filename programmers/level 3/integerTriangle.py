def solution(triangle):
    length = len(triangle)
    copy_triangle = [[0 for _ in range(1, len(triangle[p])+1)] for p in range(length)]
    for row in range(length):
        for idx in range(row + 1):
            if row == 0:
                copy_triangle[row][idx] = triangle[row][idx]
            elif idx == 0:
                copy_triangle[row][idx] = triangle[row][idx] + copy_triangle[row-1][idx]
            elif idx == row:
                copy_triangle[row][idx] = triangle[row][idx] + copy_triangle[row-1][idx-1]
            else:
                copy_triangle[row][idx] = triangle[row][idx] + max(copy_triangle[row-1][idx-1], copy_triangle[row-1][idx])
    answer = max(copy_triangle[-1])
    return answer