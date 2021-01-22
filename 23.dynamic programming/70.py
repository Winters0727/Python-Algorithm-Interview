class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0,1,2]
        for case in range(3, n+1):
            memo.append(memo[case-1] + memo[case-2])
        return memo[n]