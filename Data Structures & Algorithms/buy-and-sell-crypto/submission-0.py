class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        buy = 0
        sell = 0
        buy_price = prices[buy]
        sell_price = prices[sell]
        for i, price in enumerate(prices):
            if price < buy_price:
                buy = i
                sell = i
            elif price > sell_price:
                sell = i

            buy_price = prices[buy]
            sell_price = prices[sell]
            temp_profit = sell_price - buy_price
            if temp_profit > profit:
                profit = temp_profit

        return profit