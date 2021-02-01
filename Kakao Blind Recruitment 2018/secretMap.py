def solution(n, arr1, arr2):
    def binary_transform(n, array):
        result = []
        for value in array:
            num = bin(value)[2:]
            length = len(num)
            if length < n:
                result.append('0'*(n-length)+num)
            else:
                result.append(num)
        return result
    
    trans_arr1 = binary_transform(n, arr1)
    trans_arr2 = binary_transform(n, arr2)
    
    answer = []
    
    for i in range(n):
        answer.append(''.join(['#' if int(trans_arr1[i][j]) or int(trans_arr2[i][j]) else ' ' for j in range(n)]))
    print(answer)
    return answer