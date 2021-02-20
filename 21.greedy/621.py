from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        answer = 0
        while True:
            sub_count = 0
            
            for task, _ in counter.most_common(n+1):
                print(task)
                sub_count += 1
                answer += 1
                counter.subtract(task)
                counter += Counter()
            
            if not counter:
                break
            answer += n - sub_count + 1
        return answer