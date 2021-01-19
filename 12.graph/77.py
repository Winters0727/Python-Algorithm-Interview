class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        result, comb = [], []
        def DFS(comb, p, s, k):
            if s == k:
                result.append(comb[:])
            else:
                for j in range(p, n):
                    if nums[j] not in comb:
                        comb.append(nums[j])
                        DFS(comb, j, s+1, k)
                        comb.pop()
        DFS(comb, 0, 0, k)
        return result