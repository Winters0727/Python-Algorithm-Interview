def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        left, right = i, length-1
        while left < right:
            if s[left] != s[right]:
                answer += (right - left)
                break
    return answer