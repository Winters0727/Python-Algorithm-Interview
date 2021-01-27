class Solution:
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        left, right = 0, length-1
        for num in nums:
            if num == 0:
                left += 1
            elif num == 2:
                right -= 1
        
        for index in range(length):
            if index < left:
                nums[index] = 0
            elif index > right:
                nums[index] = 2
            else:
                nums[index] = 1