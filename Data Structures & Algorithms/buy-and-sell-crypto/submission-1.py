class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = max(prices) + 1
        sell = min(prices) - 1
        bought = False
        sold = False

        for i, price in enumerate(prices):
            if price < buy:
                buy = price
                bought = True
            elif price > sell:
                sell = price
                sold = True

        if bought and sold:
            maxProfit = sell - buy
            return maxProfit

        return 0