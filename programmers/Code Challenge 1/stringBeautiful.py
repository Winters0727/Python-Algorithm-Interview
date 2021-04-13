def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        for j in range(length-1, i, -1):
            left, right = i, j
            while left < right:
                if s[left] != s[right]:
                    answer += (right - left)
                    break
                right -= 1
    return answer