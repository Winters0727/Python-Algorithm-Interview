class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_strings = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        answer = list()
        temp_list = list()
        for digit in digits:
            if not temp_list:
                temp_list = list(digit_strings[digit])
                continue
            else:
                return_list = list()
                while temp_list:
                    prefix = temp_list.pop()
                    digit_list = digit_strings[digit]
                    for string in digit_list:
                        return_list.append(prefix + string)
                temp_list = return_list
        if temp_list:
            answer = temp_list
        return answer