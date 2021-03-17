def solution(begin, target, words):
    def compare_word(first, second):
        length = len(first)
        count = 0
        for i in range(length):
            if first[i] == second[i]:
                continue
            else:
                if count == 0:
                    count += 1
                else:
                    return False
        return True
    
    if target not in words:
        return 0
    
    answer = float('INF')
    length = len(words)
    used = [0 for _ in range(length)]
    stack = [(begin, 0, used[:])]
    while stack:
        word, count, visited = stack.pop()
        for i in range(length):
            if not visited[i] and compare_word(word, words[i]):
                if words[i] == target and count+1 < answer:
                    answer = count+1
                visited_copy = visited[:]
                visited_copy[i] = 1
                stack.append((words[i], count+1, visited_copy))
    return answer