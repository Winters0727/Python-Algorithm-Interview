from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length%2:
            maj_count = length//2 + 1
        else:
            maj_count = length//2
            
        number_count = defaultdict(int)
        for index in range(length):
            number_count[nums[index]] += 1
            if number_count[nums[index]] >= maj_count:
                return nums[index]