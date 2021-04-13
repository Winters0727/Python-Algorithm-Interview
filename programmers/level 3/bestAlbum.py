import heapq
from collections import defaultdict

def solution(genres, plays):
    answer = []
    length = len(genres)
    q = []
    genre_list = defaultdict(list)
    genre_used = defaultdict(int)
    genre_total = defaultdict(int)
    for i in range(length):
        genre_list[genres[i]].append([i, plays[i]])
        genre_total[genres[i]] += plays[i]        
    for key in genre_total.keys():
        heapq.heappush(q, (-genre_total[key], key))
    for key in genre_list.keys():
        genre_list[key].sort(key=lambda x:[x[1], -x[0]])  
        
    while q:
        _, genre = heapq.heappop(q)
        if not genre_used[genre]:
            value = genre_list[genre].pop()
            answer.append(value[0])
            if genre_list[genre]:
                value = genre_list[genre].pop()
                while genre_list[genre] and genre_list[genre][-1][1] == value[1]:
                    value = genre_list[genre].pop()
                answer.append(value[0])
            genre_used[genre] = 1
    return answer