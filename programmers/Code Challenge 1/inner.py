def solution(a, b):
    return sum([a[k]*b[k] for k in range(len(a))])