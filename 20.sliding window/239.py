class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        answer = []
        
        window = nums[:k]
        max_number = max(nums[:k])
        answer.append(max_number)
        
        for idx, val in enumerate(nums):
            if idx < k:
                continue
                
            window.append(val)

            if max_number == float('-inf'):
                max_number = max(window)
            elif max_number < val:
                max_number = val

            answer.append(max_number)
            
            if max_number == window.pop(0):
                max_number = float('-inf')
        return answer