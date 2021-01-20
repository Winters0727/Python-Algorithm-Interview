from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        case = defaultdict(list)
        for (course, pre) in prerequisites:
            case[course].append(pre)
        
        def DFS(number, heard):
            print(heard)
            if len(heard) == numCourses:
                return True
            else:
                for course in case[number]:
                    print(number not in case[course])
                    if course not in heard and number not in case[course]:
                        heard.append(number)
                        return DFS(course, heard[:])
                    else: # cyclic
                        return False

        answer = False
        for k in range(0, numCourses):
            print(answer)
            answer = DFS(k, [])
            if answer:
                break
                
        return answer