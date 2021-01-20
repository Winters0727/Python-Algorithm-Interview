class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        def calculate(left, right):
            while left >= 0 and right <= length-1 and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
            
        if len(s) < 2 or s == s[::-1]:
            return s
        
        answer = ""

        for index, char in enumerate(s):
            answer = max([answer, calculate(index, index+1), calculate(index, index+2)], key=len)
        
        return answer