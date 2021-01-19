from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        case = defaultdict(list)
        for (start, end) in sorted(tickets, reverse=True):
            case[start].append(end)
            
        result = []
        
        def DFS(start):
            while case[start]:
                DFS(case[start].pop())
            result.append(start)
                
        DFS('JFK')
        return result[::-1]