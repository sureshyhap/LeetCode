class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        while True:
            if len(prices) < 2:
                break
            i = 0
            while prices[i] > prices[i + 1]:
                i += 1
                if i + 1 == len(prices):
                    break
            prices = prices[i:]        
            minimum = 10 ** 5
            min_index = None
            maximum = 0
            max_index = None
            for i in range(len(prices)):
                if prices[i] < minimum:
                    minimum = prices[i]
                    min_index = i
            for i in range(len(prices) - 1, min_index - 1, -1):
                if prices[i] > maximum:
                    maximum = prices[i]
                    max_index = i
            profit = maximum - minimum
            if profit > max_profit:
                max_profit = profit
            prices = prices[:min_index]
        return max_profit
