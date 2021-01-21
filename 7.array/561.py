class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        answer = 0
        for index in range(0, length, 2):
            answer += nums[index]
        return answer