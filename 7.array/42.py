class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        answer = 0
        length = len(height)
        
        left, right = 0, length -1
        
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            
            if left_max <= right_max:
                answer += left_max - height[left]
                left += 1
            else:
                answer += right_max - height[right]
                right -= 1
        
        return answer