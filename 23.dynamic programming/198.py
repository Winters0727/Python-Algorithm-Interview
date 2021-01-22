class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            memo = [0 for _ in range(len(nums))]
            memo[0] = nums[0]
            memo[1] = max(nums[0], nums[1])
            for index in range(2,len(nums)):
                memo[index] = max(memo[index-1], memo[index-2]+nums[index])
            return memo[-1]