from collections import defaultdict
import heapq

INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = defaultdict(lambda:defaultdict(lambda:INF))
    for fare in fares:
        srt, dst, fee = fare
        graph[srt][dst] = fee
        graph[dst][srt] = fee
    
    def dijkstra(src, dst):
        nonlocal graph
        if src == dst:
            return 0
        queue = [[0, src]]
        table = defaultdict(lambda:INF)
        while queue:
            cost, now = heapq.heappop(queue)
            if table[now] < cost:
                continue
            for k in graph[now].keys():
                if now == k or graph[now][k] == INF:
                    continue
                if cost + graph[now][k] < table[k]:
                    table[k] = cost + graph[now][k]
                    heapq.heappush(queue, [cost + graph[now][k], k])
        return table[dst]
    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return answer