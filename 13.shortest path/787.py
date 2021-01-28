from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for (u,v,w) in flights:
            graph[u].append((v,w))
            
        queue = [(0, src, 0)]
        
        while queue:
            cost, start_node, count = heapq.heappop(queue)
            if start_node == dst:
                return cost
            if count <= K:
                for (next_node, next_cost) in graph[start_node]:
                    heapq.heappush(queue, (cost + next_cost, next_node, count+1))

        return -1