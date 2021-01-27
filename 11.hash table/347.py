from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
        answer = sorted(list(num_dict.keys()), key=lambda x : -num_dict[x])
        return answer[:k]