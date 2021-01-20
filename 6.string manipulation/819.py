from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        temp_word = ''
        for char in paragraph:
            if char.isalpha():
                temp_word += char.lower()
            else:
                if temp_word:
                    words.append(temp_word)
                    temp_word = ''
        if temp_word:
            words.append(temp_word)
            
        word_counter = defaultdict(int)
        for word in words:
            word_counter[word] += 1
        
        answer, answer_count = '', 0
        for word in word_counter:
            if word_counter[word] > answer_count and word not in banned:
                answer, answer_count = word, word_counter[word]
                
        return answer