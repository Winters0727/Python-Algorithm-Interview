class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        candidates.sort()
        result = []
        def DFS(s, case):
            for i in range(s, length):
                if sum(case) + candidates[i] < target:
                    case.append(candidates[i])
                    DFS(i, case)
                    case.pop()
                elif sum(case) + candidates[i] == target:
                    case.append(candidates[i])
                    result.append(case[:])
                    case.pop()
        DFS(0, [])
        return result