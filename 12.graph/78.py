class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        def DFS(s, count, subset):
            result.append(subset[:])
            if count == length:
                return
            for i in range(s, length):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    DFS(i, count+1, subset)
                    subset.pop()
        DFS(0, 0, [])
        return result