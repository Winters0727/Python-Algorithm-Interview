class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result, per = [], []
        def DFS(per):
            if len(per) == length:
                if per not in result:
                    result.append(per[:])
            else:
                for i in range(length):
                    if nums[i] not in per:
                        per.append(nums[i])
                        DFS(per)
                        per.pop()
        DFS(per)
        return result