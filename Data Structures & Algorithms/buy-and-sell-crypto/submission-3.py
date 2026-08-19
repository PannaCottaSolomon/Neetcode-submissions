class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = max(prices) + 1
        sell = min(prices) - 1
        bought = False
        sold = False

        for i, price in enumerate(prices):
            if price < buy:
                buy = price
                bought = True

                sell = buy
            elif price > sell:
                sell = price
                sold = True

            maxProfit = max(maxProfit, sell - buy)

        if bought and sold:
            return maxProfit
        return 0