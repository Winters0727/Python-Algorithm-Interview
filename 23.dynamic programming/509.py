class Solution:
    def fib(self, n: int) -> int:
        memo = [0,1]
        if n < 2:
            return memo[n]
        else:
            for index in range(2, n+1):
                memo.append(memo[index-1] + memo[index-2])
            return memo[-1]