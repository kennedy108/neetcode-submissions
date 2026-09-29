class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = prices[0]
        for i in prices:
            if i < smallest:
                smallest = i
            else:
                current_profit = i - smallest
                if current_profit > profit:
                    profit = current_profit
        return profit
