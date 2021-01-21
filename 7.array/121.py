class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        
        min_price = float('INF')
        
        for price in prices:
            min_price = min(price, min_price)
            answer = max(answer, price - min_price)
        
        return answer