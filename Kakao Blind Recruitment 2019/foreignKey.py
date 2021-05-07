def solution(relation):
    length = len(relation)
    relation_list = list(zip(*relation))
    N = len(relation_list)
    answer_list = []
    for i in range(1, 1 << N):
        checker = []
        for j in range(N):
            if (i & 1 << j):
                checker.append(j)
        check_list = ['-'.join([relation_list[check][n] for check in checker]) for n in range(length)]
        if len(set(check_list)) == N:
            check_case = int(''.join(['1' if num in checker else '0' for num in range(N)]), 2)
            if answer_list:
                for case in answer_list:
                    if (check_case & case) == case:
                        break
                else:
                    answer_list.append(check_case)
            else:
                answer_list.append(check_case)
    answer = len(answer_list)
    return answer