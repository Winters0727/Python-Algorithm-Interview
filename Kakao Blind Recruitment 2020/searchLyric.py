def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        query_length = len(query)
        query_check = []
        for index, char in enumerate(query):
            if char != '?':
                query_check.append(index)
        
        for word in words:
            word_length = len(word)
            if word_length != query_length:
                continue
            else:
                for index in query_check:
                    if word[index] == query[index]:
                        continue
                    else:
                        break
                else:
                    count += 1
        answer.append(count)
        
    return answer