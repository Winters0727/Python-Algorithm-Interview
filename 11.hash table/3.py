class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        data = []
        answer = 0
        for char in s:
            if char in data:
                if char == data[-1]:
                    data.clear()
                elif char == data[0]:
                    data.pop(0)
                else:
                    char_index = data.index(char)
                    data = data[char_index+1:]
            data.append(char)
            answer = max(answer, len(data))
        return answer