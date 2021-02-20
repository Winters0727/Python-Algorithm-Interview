class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        if input.isdigit():
            return [int(input)]
        
        answer = []
        
        for idx, val in enumerate(input):
            if val in '+-*':
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx + 1:])
                
                answer.extend(compute(left, right, val))
                
        return answer