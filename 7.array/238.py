class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        product = 1
        result = []
        
        for i in range(length):
            result.append(product)
            product *= nums[i]
        
        product = 1
        
        for j in range(length-1, -1, -1):
            result[j] = result[j]*product
            product *= nums[j]
            
        return result