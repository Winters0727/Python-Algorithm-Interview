def solution(arr):
    value_counter = {'0':0, '1':0}
    def quarter_arr(arr):
        length = len(arr)
        if length >= 4:
            half_len = length // 2
            arr_list = []
            for col in range(2):
                for row in range(2):
                    arr_list.append([arr[row*half_len+row_count][col*half_len:(col+1)*half_len] for row_count in range(half_len)])
            return arr_list
        else:
            return []

    def check_sum(arr):
        length = len(arr)
        pow_len = pow(length, 2)
        sum_val = sum([sum(row) for row in arr])
        if sum_val == 0 or sum_val == pow_len:
            if sum_val == 0:
                value_counter['0'] += 1
            else:
                value_counter['1'] += 1
        else:
            if length == 2:
                for row in range(2):
                    for col in range(2):
                        value_counter[str(arr[row][col])] += 1
            else:
                new_arr_list = quarter_arr(arr)
                for new_arr in new_arr_list:
                    check_sum(new_arr)
    check_sum(arr)
    answer = [value_counter['0'], value_counter['1']]
    return answer