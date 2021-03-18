import heapq
from collections import defaultdict

def solution(genres, plays):
    answer = []
    length = len(genres)
    q = []
    genre_list = defaultdict(list)
    genre_used = defaultdict(int)
    for i in range(length):
        genre_list[genres[i]].append([i, plays[i]])
        heapq.heappush(q, (-plays[i], genres[i]))
    for key in genre_list.keys():
        genre_list[key].sort(key=lambda x:x[1])
        
    while q:
        _, genre = heapq.heappop(q)
        if not genre_used[genre]:
            value = genre_list[genre].pop()
            while genre_list[genre] and genre_list[genre][-1][1] == value[1]:
                value = genre_list[genre].pop()
            answer.append(value[0])
            if genre_list[genre]:
                value = genre_list[genre].pop()
                while genre_list[genre] and genre_list[genre][-1][1] == value[1]:
                    value = genre_list[genre].pop()
                answer.append(value[0])
            genre_used[genre] = 1
    return answer