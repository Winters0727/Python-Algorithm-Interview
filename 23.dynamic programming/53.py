class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = nums[0], 0
        
        for index in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[index]
            max_sum = max(max_sum, cur_sum)
            
        return max_sum