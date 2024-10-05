class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        count = 1
        while self.prices and price >= self.prices[-1][0]:
            count += self.prices[-1][1]
            self.prices.pop()
        self.prices.append((price, count))
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
