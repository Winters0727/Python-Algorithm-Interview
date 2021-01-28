from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for (u, v, w) in times:
            graph[u].append((v,w)) # (node, time)
        
        visited = [k]
        
        node_time = defaultdict(int)
        queue = [(0,k)] # (time, node)
        while queue:
            time, node = heapq.heappop(queue)
            if node not in visited:
                visited.append(node)
                node_time[node] = time
            for (des_node, took_time) in graph[node]:
                if des_node not in visited:
                    heapq.heappush(queue, (time+took_time, des_node))
                    
        if len(visited) == n:
            return max(node_time.values())
        return -1