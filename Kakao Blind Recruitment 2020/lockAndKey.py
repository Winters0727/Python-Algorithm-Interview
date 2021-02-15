def solution(key, lock):
    def rotate_key(key): # rotate 90 degrees
        length = len(key)
        rotate = [[0]*length for _ in range(length)]
        for row in range(length):
            for col in range(length):
                rotate[col][length-1-row] = key[row][col]
        return rotate

    def check_lock(key, temp_lock):
        length = len(key)
        wrong_key = False
        for _ in range(4):
            for row in range(length):
                for col in range(length):
                    if key[row][col] or temp_lock[row][col]:
                        continue
                    else:
                        wrong_key = True
                        break
                if wrong_key:
                    wrong_key = False
                    break
            else:
                return True
            key = rotate_key(key)
        return False

    M, N = len(key), len(lock)
    large_lock = []
    for _ in range(N-1):
        large_lock.append([0 for _ in range(3*N-2)])
        
    for i in range(N):
        large_lock.append([0]*(N-1) + lock[i] + [0]*(N-1))
        
    for _ in range(N-1):
        large_lock.append([0 for _ in range(3*N-2)])
    
    for row in range(2*N-2):
        for col in range(2*N-2):
            temp_lock = []
            for k in range(M):
                temp_lock.append(large_lock[row + k][col:col+M][:])

            result = check_lock(key, temp_lock)
            if result:
                return True
    return False