from collections import defaultdict # False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        case = defaultdict(list)
        for (course, pre) in prerequisites:
            case[course].append(pre)
        
        def DFS(number, heard):
            heard.append(number)
            print(heard)
            print(len(heard), numCourses)
            print(len(heard) == numCourses)
            if len(heard) == numCourses:
                return True
            
            for course in case[number]:
                if course not in heard:
                    DFS(course, heard)
            
        answer = False
        for k in range(1, numCourses):
            answer = DFS(k, [])

            if answer:
                break
                
        return answer