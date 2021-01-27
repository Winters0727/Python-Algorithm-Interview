from collections import defaultdict

class compareNumber(str):
    def __lt__(x,y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return ""
        elif len(nums) == 1:
            return str(nums[0])
        else:
            answer = ""
            numbers = defaultdict(list)

            for num in nums:
                numbers[int(str(num)[0])].append(str(num))

            for case in range(9, -1, -1):
                if numbers[case]:
                    numbers[case].sort(reverse=True, key=compareNumber)
                    
                    while numbers[case]:
                        answer += numbers[case].pop()
                        
            if len(answer) == list(answer).count('0'):
                return '0'

            return answer