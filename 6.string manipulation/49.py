from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_counter = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            anagram_counter[sorted_word].append(word)
        
        return list(anagram_counter.values())