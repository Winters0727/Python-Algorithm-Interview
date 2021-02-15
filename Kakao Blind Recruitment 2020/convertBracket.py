def solution(p):
    answer = ''

    def check_bracket(p):
        open_counter = 0
        for b in p:
            if b == '(':
                open_counter += 1
            elif b == ')':
                if open_counter > 0:
                    open_counter -= 1
                else:
                    return False
        return True

    def check_equal(p):
        if p.count('(') == p.count(')'):
            return True
        return False

    def simul(p, answer):
        if not p or check_bracket(p):
            return p
        
        pointer = 2
        while True:
            u, v = p[:pointer], p[pointer:]
            if not check_equal(u):
                pointer += 2
                continue
            else:
                if check_bracket(u):
                    answer += u
                    return simul(v, answer)
                else:
                    u_len = len(u) // 2
                    return answer + ('('*u_len + ')'*u_len + simul(v,answer))

    if check_bracket(p):
        return p

    answer = simul(p, answer)
    return answer