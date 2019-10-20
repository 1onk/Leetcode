class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        i, j = 0, 0
        res = 0
        min_price = prices[0]
        for price in prices:
            res = max(price - min_price, res)
            min_price = min(price, min_price)
        return res