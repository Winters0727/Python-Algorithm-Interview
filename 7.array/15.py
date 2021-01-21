class Solution: # Too slow...
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        
        if length < 3:
            return []
        
        result = []
        
        for index in range(1, length-1):
            left, right = index-1, index+1
            while 0 <= left and right <= length-1:
                case = nums[left] + nums[index] + nums[right]
                if case > 0:
                    left -= 1
                elif case < 0:
                    right += 1
                else:
                    answer_case = [nums[left], nums[index], nums[right]]
                    if answer_case not in result:
                        result.append(answer_case)
                    left -= 1
                    right += 1
            
        return result