def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x : x[2])
    visited = set()
    check_table = {str(num):num for num in range(n)}
    for cost in costs:
        if sum(check_table.values()) == 0:
            break
        i1, i2, c = cost
        if i1 in visited and i2 in visited:
            if check_table[str(i1)] == check_table[str(i2)]:
                continue
            else:
                min_table = min(check_table[str(i1)], check_table[str(i2)])
                check_table[str(i1)], check_table[str(i2)] = min_table, min_table
                answer += c
        else:
            visited.add(i1)
            visited.add(i2)
            min_table = min(check_table[str(i1)], check_table[str(i2)])
            check_table[str(i1)], check_table[str(i2)] = min_table, min_table
            answer += c
    return answer