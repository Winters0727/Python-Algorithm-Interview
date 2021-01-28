from collections import defaultdict

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        answer = 0
        while s and g:
            if s[-1] < g[-1]:
                g.pop()
            else:
                answer += 1
                s.pop()
                g.pop()
        return answer